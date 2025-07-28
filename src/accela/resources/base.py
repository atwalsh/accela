import json
import re
from abc import ABC
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Dict, Generic, Iterator, List, Optional, Type, TypeVar, Union
from zoneinfo import ZoneInfo

import requests

T = TypeVar("T")


class ResourceModel(ABC):
    """Abstract base class for Accela API models with common functionality."""

    FIELD_MAPPING: Dict[str, str]  # Required mapping of {"apiField": "python_field"}
    # Optional field type mapping
    DICT_FIELDS: List[str] = []  # API fields containing objects that need snake_case key conversion
    DATETIME_FIELDS: List[str] = []  # API fields that should be parsed as datetime objects
    BOOL_FIELDS: List[str] = []  # API fields that contain 'Y'/'N' strings to convert to boolean

    @classmethod
    def _camel_to_snake(cls, name: str) -> str:
        """Convert camelCase to snake_case."""
        # Insert underscore before uppercase letters that follow lowercase letters
        s1 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
        return s1.lower()

    @classmethod
    def _convert_keys_to_snake_case(cls, obj: Union[Dict, List, Any]) -> Union[Dict, List, Any]:
        """Recursively convert all dictionary keys from camelCase to snake_case."""
        if isinstance(obj, dict):
            return {
                cls._camel_to_snake(key): cls._convert_keys_to_snake_case(value)
                for key, value in obj.items()
            }
        elif isinstance(obj, list):
            return [cls._convert_keys_to_snake_case(item) for item in obj]
        else:
            return obj

    @classmethod
    def _parse_bool(cls, bool_str: str) -> bool:
        """Parse Accela boolean string to boolean object.

        Args:
            bool_str: Boolean string, typically 'Y' for True, 'N' or anything else for False

        Returns:
            bool: True if 'Y', False otherwise
        """
        return bool_str.upper() == "Y"

    @classmethod
    def _parse_datetime(cls, date_str: str, timezone: Optional[ZoneInfo] = None) -> datetime:
        """Parse Accela datetime string to datetime object.

        Args:
            date_str: Datetime string in format "YYYY-MM-DD HH:MM:SS"
            timezone: Optional timezone to apply to the naive datetime

        Returns:
            datetime object, naive or timezone-aware based on timezone parameter
        """
        # Parse the datetime string
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        if timezone:
            dt = dt.replace(tzinfo=timezone)
        return dt

    @classmethod
    def from_json(cls, data: Dict[str, Any], client=None):
        """Generic method to create instance from API response data."""
        kwargs = {}

        for api_field, python_field in cls.FIELD_MAPPING.items():
            if api_field in data:
                value = data[api_field]

                # Apply recursive snake_case conversion for dictionary object fields
                if api_field in cls.DICT_FIELDS:
                    value = cls._convert_keys_to_snake_case(value)

                # Parse datetime fields
                elif (
                        api_field in cls.DATETIME_FIELDS
                        and value is not None
                        and isinstance(value, str)
                ):
                    timezone = client.timezone if client else None
                    value = cls._parse_datetime(value, timezone)

                # Parse boolean fields
                elif (
                        api_field in cls.BOOL_FIELDS
                        and value is not None
                        and isinstance(value, str)
                ):
                    value = cls._parse_bool(value)

                kwargs[python_field] = value

        instance = cls(**kwargs)  # type: ignore
        instance.raw_json = data
        return instance

    def to_dict(self) -> Dict[str, Any]:
        result = {}
        for key, value in asdict(self).items():  # noqa
            if key != "raw_json":
                result[key] = value
        return result

    def to_json(self, pretty: bool = False) -> str:
        indent = 2 if pretty else None
        return json.dumps(self.to_dict(), indent=indent, default=str)

    def __str__(self) -> str:
        return self.to_json(pretty=False)


@dataclass
class ListResponse(Generic[T]):
    """Generic container for a list of items with pagination support."""

    data: List[T]
    has_more: bool
    offset: int
    limit: int
    total: int
    _client: Any = None
    _params: Dict[str, Any] = field(default_factory=dict)
    _url: str = None
    _model_class: Type[T] = None

    def auto_paging_iter(self) -> Iterator[T]:
        """Automatically handle pagination and yield items one at a time."""
        yield from self.data

        # Continue fetching more pages as long as there are more items
        while self.has_more:
            self._params["offset"] = self.offset + self.limit

            response = requests.get(
                self._url, headers=self._client.headers, params=self._params
            )
            response.raise_for_status()

            result = response.json()
            # Handle case where result key is missing (empty response)
            if "result" not in result:
                items = []
            else:
                items = [
                    self._model_class.from_json(item, self._client)
                    for item in result["result"]
                ]

            # Update this instance with new page info
            self.data = items
            self.offset += self.limit
            self.has_more = len(items) == self.limit and self.offset < self.total

            # Yield items from this page
            yield from items

    def __iter__(self) -> Iterator[T]:
        return iter(self.data)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "data": [
                item.to_dict() if hasattr(item, "to_dict") else item
                for item in self.data
            ],
            "has_more": self.has_more,
            "offset": self.offset,
            "limit": self.limit,
            "total": self.total,
        }

    def to_json(self, pretty: bool = False) -> str:
        indent = 2 if pretty else None
        return json.dumps(self.to_dict(), indent=indent, default=str)

    def __str__(self) -> str:
        return f"ListResponse(total={self.total}, offset={self.offset}, limit={self.limit}, has_more={self.has_more})"


class BaseResource:
    """Base class for all Accela API resources."""
    
    # Override in subclasses to specify required client attributes
    # For example, the /agencies/ endpoint requires a token, but not an environment or agency
    REQUIRES_AGENCY = True
    REQUIRES_ENVIRONMENT = True

    def __init__(self, client):
        """Initialize the resource with an AccelaClient instance."""
        self.client = client
        self._validate_client_requirements()
    
    def _validate_client_requirements(self):
        """Validate that the client has required attributes for this resource."""
        if self.REQUIRES_AGENCY and not self.client.agency:
            raise ValueError(
                f"{self.__class__.__name__} requires an agency. "
                f"Initialize AccelaClient with agency parameter: "
                f"AccelaClient(access_token='...', agency='AGENCY_NAME', environment='ENV')"
            )
        if self.REQUIRES_ENVIRONMENT and not self.client.environment:
            raise ValueError(
                f"{self.__class__.__name__} requires an environment. "
                f"Initialize AccelaClient with environment parameter: "
                f"AccelaClient(access_token='...', agency='AGENCY_NAME', environment='ENV')"
            )

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request to the Accela API.

        Args:
            url: The API endpoint URL
            params: Optional query parameters

        Returns:
            The JSON response from the API

        Raises:
            requests.HTTPError: If the request fails
        """
        response = requests.get(url, headers=self.client.headers, params=params)
        response.raise_for_status()
        return response.json()

    def _get_binary(
            self, url: str, params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """Make a GET request that returns binary content.

        Args:
            url: The API endpoint URL
            params: Optional query parameters

        Returns:
            The raw Response object for binary content access

        Raises:
            requests.HTTPError: If the request fails
        """
        response = requests.get(url, headers=self.client.headers, params=params)
        response.raise_for_status()
        return response

    def _list_resource(self, url: str, model_class: Type[T], params: Dict[str, Any], result_key: str = "result") -> \
    ListResponse[T]:
        """Generic method to list resources with pagination support.

        Args:
            url: The API endpoint URL
            model_class: The model class to use for parsing results
            params: Query parameters including limit and offset
            result_key: The key in the response that contains the results array

        Returns:
            ListResponse object with pagination support
        """
        limit = params.get("limit", 100)
        offset = params.get("offset", 0)

        result = self._get(url, params=params)

        # Parse the results into model instances
        # Handle case where result key is missing (empty response)
        if result_key not in result:
            items = []
        else:
            items = [model_class.from_json(item, self.client) for item in result[result_key]]
        total = result.get("total", len(items))

        return ListResponse(
            data=items,
            has_more=len(items) == limit and offset + limit < total,
            offset=offset,
            limit=limit,
            total=total,
            _client=self.client,
            _params=params,
            _url=url,
            _model_class=model_class,
        )  # Type will be inferred as ListResponse[model_class]

    def _make_request(self, method: str, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a request to the Accela API.

        Note: Currently only GET requests are fully supported and tested.

        Args:
            method: HTTP method (GET, POST, etc.)
            url: The API endpoint URL
            params: Optional query parameters

        Returns:
            The JSON response from the API

        Raises:
            ValueError: If an unsupported HTTP method is specified
            requests.HTTPError: If the request fails
        """
        # For now, we're only supporting GET requests
        if method.upper() == "GET":
            return self._get(url, params)
        else:
            raise ValueError(f"Method {method} is not currently supported")

from dataclasses import dataclass, field
from typing import Any, Dict, Generic, Iterator, List, Optional, Type, TypeVar

import requests

T = TypeVar("T")


class ResourceModel:
    """Mixin class for Accela API models with common functionality."""

    @classmethod
    def from_json(cls, data: Dict[str, Any]):
        """Create a model instance from API response data."""
        raise NotImplementedError("Subclasses must implement from_json")


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
            items = [self._model_class.from_json(item) for item in result["result"]]

            # Update this instance with new page info
            self.data = items
            self.offset += self.limit
            self.has_more = len(items) == self.limit and self.offset < self.total

            # Yield items from this page
            yield from items

    def __iter__(self) -> Iterator[T]:
        """Make the object iterable, returning just the current page of data."""
        return iter(self.data)


class BaseResource:
    """Base class for all Accela API resources."""

    def __init__(self, client):
        """Initialize the resource with an AccelaClient instance."""
        self.client = client

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

    def _list_resource(
        self,
        url: str,
        model_class: Type[T],
        params: Dict[str, Any],
        result_key: str = "result",
    ) -> ListResponse[T]:
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
        items = [model_class.from_json(item) for item in result[result_key]]
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

    def _make_request(
        self, method: str, url: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
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

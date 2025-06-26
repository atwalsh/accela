from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, Dict

from .base import BaseResource, ListResponse, ResourceModel
from .record_addresses import RecordAddresses
from .record_documents import RecordDocuments


@dataclass
class Record(ResourceModel):
    """Represents an Accela record."""

    id: str
    module: str
    opened_date: date
    type: str
    name: str = ""
    description: str = ""
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "Record":
        """Create a Record instance from API response data."""
        return cls(
            id=data["id"],
            module=data["module"],
            opened_date=datetime.strptime(
                data["openedDate"], "%Y-%m-%d %H:%M:%S"
            ).date(),
            type=data["type"]["value"],
            name=data.get("name", ""),
            description=data.get("description", ""),
            raw_json=data,
        )


class Records(BaseResource):
    """Records resource for interacting with Accela records API."""

    def __init__(self, client):
        """Initialize the Records resource with an AccelaClient instance."""
        super().__init__(client)
        self.addresses = RecordAddresses(client)
        self.documents = RecordDocuments(client)

    def list(
        self,
        limit: int = 100,
        offset: int = 0,
        module: str = None,
        record_type: str = None,
        opened_date_after: date = None,
    ) -> ListResponse[Record]:
        """
        List records with pagination support.

        Args:
            limit: Number of records per page, default 100
            offset: Starting offset for pagination, default 0
            module: Filter records by module name
            record_type: Filter records by record type
            opened_date_after: Filter records opened on or after this date

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/records"
        params = {"limit": limit, "offset": offset}

        # Add filters if provided
        if module:
            params["module"] = module

        if record_type:
            params["type"] = record_type

        if opened_date_after:
            # Format date as YYYY-MM-DD for the API
            params["openedDateFrom"] = opened_date_after.strftime("%Y-%m-%d")

        # Use the generic list method from BaseResource
        return self._list_resource(url, Record, params)

    def retrieve(self, record_id: str) -> Record:
        """
        Retrieve a specific record by ID.

        Args:
            record_id: The ID of the record to retrieve

        Returns:
            Record object
        """
        url = f"{self.client.BASE_URL}/records/{record_id}"
        result = self._get(url)
        return Record.from_json(result["result"][0])

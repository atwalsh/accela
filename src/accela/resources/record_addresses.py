from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordAddress(ResourceModel):
    """Represents an address associated with an Accela record."""

    street_name: str
    street_number: str
    city: str
    state: str
    postal_code: str
    country: Optional[str] = None
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "RecordAddress":
        """Create a RecordAddress instance from API response data."""
        return cls(
            street_name=data.get("streetName", ""),
            street_number=data.get("streetStart", ""),
            city=data.get("city", ""),
            state=data.get("state", ""),
            postal_code=data.get("postalCode", ""),
            country=data.get("country", None),
            raw_json=data,
        )


class RecordAddresses(BaseResource):
    """Resource for interacting with Accela record addresses."""

    def list(
        self, record_id: str, limit: int = 100, offset: int = 0
    ) -> ListResponse[RecordAddress]:
        """
        List all addresses associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get addresses for
            limit: Number of addresses per page, default 100
            offset: Starting offset for pagination, default 0

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/addresses"
        params = {"limit": limit, "offset": offset}

        return self._list_resource(url, RecordAddress, params)

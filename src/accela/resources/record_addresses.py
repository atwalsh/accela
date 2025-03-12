from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordAddress(ResourceModel):
    """Represents an address associated with an Accela record."""

    street_name: str
    street_start: str
    city: str
    state: str
    postal_code: str
    county: str
    street_suffix: str
    id: str
    is_primary: bool
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "RecordAddress":
        """Create a RecordAddress instance from API response data."""
        # Handle nested objects like state and streetSuffix
        state = data.get("state", {})
        state_value = state.get("value", "") if isinstance(state, dict) else state

        street_suffix = data.get("streetSuffix", {})
        street_suffix_value = (
            street_suffix.get("value", "")
            if isinstance(street_suffix, dict)
            else street_suffix
        )

        # Convert isPrimary from "Y"/"N" to boolean
        is_primary = data.get("isPrimary", "N") == "Y"

        return cls(
            id=str(data.get("id", "")),
            street_name=data.get("streetName", ""),
            street_start=str(data.get("streetStart", "")),
            city=data.get("city", ""),
            state=state_value,
            postal_code=data.get("postalCode", ""),
            county=data.get("county", ""),
            street_suffix=street_suffix_value,
            is_primary=is_primary,
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

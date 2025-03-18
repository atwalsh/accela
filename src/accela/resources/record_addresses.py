from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordAddress(ResourceModel):
    """Represents an address associated with an Accela record."""

    id: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    county: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    distance: Optional[float] = None
    house_alpha_start: Optional[str] = None
    house_alpha_end: Optional[str] = None
    inspection_district: Optional[str] = None
    inspection_district_prefix: Optional[str] = None
    is_primary: bool = False
    level_end: Optional[str] = None
    level_prefix: Optional[str] = None
    level_start: Optional[str] = None
    location_type: Optional[str] = None
    neighborhood: Optional[str] = None
    neighborhood_prefix: Optional[str] = None
    postal_code: Optional[str] = None
    record_id: Optional[str] = None
    ref_address_id: Optional[str] = None
    secondary_street: Optional[str] = None
    secondary_street_number: Optional[int] = None
    service_provider_code: Optional[str] = None
    street_address: Optional[str] = None
    street_end: Optional[int] = None
    street_end_from: Optional[int] = None
    street_end_to: Optional[int] = None
    street_name: Optional[str] = None
    street_name_start: Optional[str] = None
    street_name_end: Optional[str] = None
    street_prefix: Optional[str] = None
    street_start: Optional[int] = None
    street_start_from: Optional[int] = None
    street_start_to: Optional[int] = None
    unit_start: Optional[str] = None
    unit_end: Optional[str] = None
    x_coordinate: Optional[float] = None
    y_coordinate: Optional[float] = None
    cross_street_name_start: Optional[str] = None
    cross_street_name_end: Optional[str] = None

    # Complex objects (represented as dictionaries with text/value pairs)
    address_type_flag: Optional[Dict[str, str]] = None
    direction: Optional[Dict[str, str]] = None
    house_fraction_start: Optional[Dict[str, str]] = None
    house_fraction_end: Optional[Dict[str, str]] = None
    state: Optional[Dict[str, str]] = None
    status: Optional[Dict[str, str]] = None
    street_suffix: Optional[Dict[str, str]] = None
    street_suffix_direction: Optional[Dict[str, str]] = None
    type: Optional[Dict[str, str]] = None
    unit_type: Optional[Dict[str, str]] = None

    # Store the original JSON response
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "RecordAddress":
        """Create a RecordAddress instance from API response data."""
        # Convert isPrimary from "Y"/"N" to boolean
        is_primary = data.get("isPrimary", "N") == "Y"

        # Handle nested objects
        complex_fields = [
            "addressTypeFlag",
            "direction",
            "houseFractionStart",
            "houseFractionEnd",
            "state",
            "status",
            "streetSuffix",
            "streetSuffixDirection",
            "type",
            "unitType",
            "country",
        ]

        # Create a dictionary to store all the fields
        fields = {
            "is_primary": is_primary,
            "raw_json": data,
        }

        # Map camelCase to snake_case for simple fields
        field_mapping = {
            "id": "id",
            "addressLine1": "address_line1",
            "addressLine2": "address_line2",
            "city": "city",
            "county": "county",
            "description": "description",
            "distance": "distance",
            "houseAlphaStart": "house_alpha_start",
            "houseAlphaEnd": "house_alpha_end",
            "inspectionDistrict": "inspection_district",
            "inspectionDistrictPrefix": "inspection_district_prefix",
            "levelEnd": "level_end",
            "levelPrefix": "level_prefix",
            "levelStart": "level_start",
            "locationType": "location_type",
            "neighborhood": "neighborhood",
            "neighborhoodPrefix": "neighborhood_prefix",
            "postalCode": "postal_code",
            "refAddressId": "ref_address_id",
            "secondaryStreet": "secondary_street",
            "secondaryStreetNumber": "secondary_street_number",
            "serviceProviderCode": "service_provider_code",
            "streetAddress": "street_address",
            "streetEnd": "street_end",
            "streetEndFrom": "street_end_from",
            "streetEndTo": "street_end_to",
            "streetName": "street_name",
            "streetNameStart": "street_name_start",
            "streetNameEnd": "street_name_end",
            "streetPrefix": "street_prefix",
            "streetStart": "street_start",
            "streetStartFrom": "street_start_from",
            "streetStartTo": "street_start_to",
            "unitStart": "unit_start",
            "unitEnd": "unit_end",
            "xCoordinate": "x_coordinate",
            "yCoordinate": "y_coordinate",
            "crossStreetNameStart": "cross_street_name_start",
            "crossStreetNameEnd": "cross_street_name_end",
        }

        # Process simple fields
        for json_field, python_field in field_mapping.items():
            if json_field in data:
                fields[python_field] = data.get(json_field)

        # Process complex fields (text/value objects)
        for field in complex_fields:
            snake_field = "".join(
                ["_" + c.lower() if c.isupper() else c for c in field]
            ).lstrip("_")
            if field in data and isinstance(data[field], dict):
                fields[snake_field] = data[field]

        # Handle recordId separately if it exists
        if "recordId" in data:
            fields["record_id"] = (
                data["recordId"].get("id")
                if isinstance(data["recordId"], dict)
                else data["recordId"]
            )

        return cls(**fields)


class RecordAddresses(BaseResource):
    """Resource for interacting with Accela record addresses."""

    def list(
        self,
        record_id: str,
        is_primary: Optional[str] = None,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> ListResponse[RecordAddress]:
        """
        List all addresses associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get addresses for
            is_primary: Filter by the primary address flag
            fields: List of fields to include in the response
            limit: Number of addresses per page, default 100
            offset: Starting offset for pagination, default 0

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/addresses"
        params = {"limit": limit, "offset": offset}

        if is_primary is not None:
            params["isPrimary"] = is_primary

        if fields is not None and len(fields) > 0:
            params["fields"] = ",".join(fields)

        return self._list_resource(url, RecordAddress, params)

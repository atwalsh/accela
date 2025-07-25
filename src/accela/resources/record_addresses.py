from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordAddress(ResourceModel):
    """Represents an address associated with an Accela record."""

    id: int
    raw_json: Dict[str, Any] = field(default_factory=dict)

    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    address_type_flag: Optional[Dict[str, Any]] = None
    city: Optional[str] = None
    country: Optional[Dict[str, Any]] = None
    county: Optional[str] = None
    cross_street_name_end: Optional[str] = None
    cross_street_name_start: Optional[str] = None
    description: Optional[str] = None
    direction: Optional[Dict[str, Any]] = None
    distance: Optional[float] = None
    house_alpha_end: Optional[str] = None
    house_alpha_start: Optional[str] = None
    house_fraction_end: Optional[Dict[str, Any]] = None
    house_fraction_start: Optional[Dict[str, Any]] = None
    inspection_district: Optional[str] = None
    inspection_district_prefix: Optional[str] = None
    is_primary: Optional[bool] = None
    level_end: Optional[str] = None
    level_prefix: Optional[str] = None
    level_start: Optional[str] = None
    location_type: Optional[str] = None
    neighborhood: Optional[str] = None
    neighborhood_prefix: Optional[str] = None
    postal_code: Optional[str] = None
    record_id: Optional[Dict[str, Any]] = None
    ref_address_id: Optional[int] = None
    secondary_street: Optional[str] = None
    secondary_street_number: Optional[int] = None
    service_provider_code: Optional[str] = None
    state: Optional[Dict[str, Any]] = None
    status: Optional[Dict[str, Any]] = None
    street_address: Optional[str] = None
    street_end: Optional[int] = None
    street_end_from: Optional[int] = None
    street_end_to: Optional[int] = None
    street_name: Optional[str] = None
    street_name_end: Optional[str] = None
    street_name_start: Optional[str] = None
    street_prefix: Optional[str] = None
    street_start: Optional[int] = None
    street_start_from: Optional[int] = None
    street_start_to: Optional[int] = None
    street_suffix: Optional[Dict[str, Any]] = None
    street_suffix_direction: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    unit_end: Optional[str] = None
    unit_start: Optional[str] = None
    unit_type: Optional[Dict[str, Any]] = None
    x_coordinate: Optional[float] = None
    y_coordinate: Optional[float] = None

    FIELD_MAPPING = {
        "addressLine1": "address_line1",
        "addressLine2": "address_line2",
        "addressTypeFlag": "address_type_flag",
        "city": "city",
        "country": "country",
        "county": "county",
        "crossStreetNameEnd": "cross_street_name_end",
        "crossStreetNameStart": "cross_street_name_start",
        "description": "description",
        "direction": "direction",
        "distance": "distance",
        "houseAlphaEnd": "house_alpha_end",
        "houseAlphaStart": "house_alpha_start",
        "houseFractionEnd": "house_fraction_end",
        "houseFractionStart": "house_fraction_start",
        "id": "id",
        "inspectionDistrict": "inspection_district",
        "inspectionDistrictPrefix": "inspection_district_prefix",
        "isPrimary": "is_primary",
        "levelEnd": "level_end",
        "levelPrefix": "level_prefix",
        "levelStart": "level_start",
        "locationType": "location_type",
        "neighborhood": "neighborhood",
        "neighborhoodPrefix": "neighborhood_prefix",
        "postalCode": "postal_code",
        "recordId": "record_id",
        "refAddressId": "ref_address_id",
        "secondaryStreet": "secondary_street",
        "secondaryStreetNumber": "secondary_street_number",
        "serviceProviderCode": "service_provider_code",
        "state": "state",
        "status": "status",
        "streetAddress": "street_address",
        "streetEnd": "street_end",
        "streetEndFrom": "street_end_from",
        "streetEndTo": "street_end_to",
        "streetName": "street_name",
        "streetNameEnd": "street_name_end",
        "streetNameStart": "street_name_start",
        "streetPrefix": "street_prefix",
        "streetStart": "street_start",
        "streetStartFrom": "street_start_from",
        "streetStartTo": "street_start_to",
        "streetSuffix": "street_suffix",
        "streetSuffixDirection": "street_suffix_direction",
        "type": "type",
        "unitEnd": "unit_end",
        "unitStart": "unit_start",
        "unitType": "unit_type",
        "xCoordinate": "x_coordinate",
        "yCoordinate": "y_coordinate",
    }

    DICT_FIELDS = [
        "addressTypeFlag",
        "country",
        "direction",
        "houseFractionEnd",
        "houseFractionStart",
        "recordId",
        "state",
        "status",
        "streetSuffix",
        "streetSuffixDirection",
        "type",
        "unitType",
    ]

    BOOL_FIELDS = [
        "isPrimary",
    ]


class RecordAddresses(BaseResource):
    """Resource for interacting with Accela record addresses."""

    def list(self, record_id: str, is_primary: Optional[str] = None, fields: Optional[List[str]] = None,
             limit: int = 100, offset: int = 0) -> ListResponse[RecordAddress]:
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
        params: Dict[str, Union[int, str]] = {"limit": limit, "offset": offset}

        if is_primary is not None:
            params["isPrimary"] = is_primary

        if fields is not None and len(fields) > 0:
            params["fields"] = ",".join(fields)

        return self._list_resource(url, RecordAddress, params)

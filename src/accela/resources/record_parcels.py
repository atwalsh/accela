from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordParcel(ResourceModel):
    """Represents a parcel associated with an Accela record."""

    id: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    block: Optional[str] = None
    book: Optional[str] = None
    census_tract: Optional[str] = None
    council_district: Optional[str] = None
    exemption_value: Optional[float] = None
    gis_sequence_number: Optional[int] = None
    improved_value: Optional[float] = None
    is_primary: Optional[bool] = None
    land_value: Optional[float] = None
    legal_description: Optional[str] = None
    lot: Optional[str] = None
    map_number: Optional[str] = None
    map_reference_info: Optional[str] = None
    owners: Optional[List[Dict[str, Any]]] = None
    page: Optional[str] = None
    parcel: Optional[str] = None
    parcel_area: Optional[float] = None
    parcel_number: Optional[str] = None
    plan_area: Optional[str] = None
    range: Optional[str] = None
    record_id: Optional[Dict[str, Any]] = None
    section: Optional[int] = None
    status: Optional[Dict[str, Any]] = None
    subdivision: Optional[Dict[str, Any]] = None
    supervisor_district: Optional[str] = None
    township: Optional[str] = None
    tract: Optional[str] = None

    FIELD_MAPPING = {
        "block": "block",
        "book": "book",
        "censusTract": "census_tract",
        "councilDistrict": "council_district",
        "exemptionValue": "exemption_value",
        "gisSequenceNumber": "gis_sequence_number",
        "id": "id",
        "improvedValue": "improved_value",
        "isPrimary": "is_primary",
        "landValue": "land_value",
        "legalDescription": "legal_description",
        "lot": "lot",
        "mapNumber": "map_number",
        "mapReferenceInfo": "map_reference_info",
        "owners": "owners",
        "page": "page",
        "parcel": "parcel",
        "parcelArea": "parcel_area",
        "parcelNumber": "parcel_number",
        "planArea": "plan_area",
        "range": "range",
        "recordId": "record_id",
        "section": "section",
        "status": "status",
        "subdivision": "subdivision",
        "supervisorDistrict": "supervisor_district",
        "township": "township",
        "tract": "tract",
    }

    DICT_FIELDS = ["owners", "recordId", "status", "subdivision"]

    BOOL_FIELDS = [
        "isPrimary",
    ]


class RecordParcels(BaseResource):
    """Resource for interacting with Accela record parcels."""

    def list(self, record_id: str, limit: int = 100, offset: int = 0) -> ListResponse[RecordParcel]:
        """
        List all parcels associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get parcels for
            limit: Number of parcels per page, default 100
            offset: Starting offset for pagination, default 0

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/parcels"
        params: Dict[str, Union[int, str]] = {"limit": limit, "offset": offset}

        return self._list_resource(url, RecordParcel, params)

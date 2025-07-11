from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordParcel(ResourceModel):
    """Represents a parcel associated with an Accela record."""

    id: Optional[str] = None
    block: Optional[str] = None
    book: Optional[str] = None
    census_tract: Optional[str] = None
    council_district: Optional[str] = None
    exemption_value: Optional[float] = None
    gis_sequence_number: Optional[int] = None
    improved_value: Optional[float] = None
    is_primary: Optional[str] = None
    land_value: Optional[float] = None
    legal_description: Optional[str] = None
    lot: Optional[str] = None
    map_number: Optional[str] = None
    map_reference_info: Optional[str] = None
    page: Optional[str] = None
    parcel: Optional[str] = None
    parcel_area: Optional[float] = None
    parcel_number: Optional[str] = None
    plan_area: Optional[str] = None
    range: Optional[str] = None
    section: Optional[int] = None
    supervisor_district: Optional[str] = None
    township: Optional[str] = None
    tract: Optional[str] = None

    status: Optional[Dict[str, Any]] = None
    subdivision: Optional[Dict[str, Any]] = None
    owners: Optional[List[Dict[str, Any]]] = None
    record_id: Optional[Dict[str, Any]] = None

    # Store the original JSON response
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "RecordParcel":
        """Create a RecordParcel instance from API response data."""
        fields = {
            "raw_json": data,
        }

        field_mapping = {
            "id": "id",
            "block": "block",
            "book": "book",
            "censusTract": "census_tract",
            "councilDistrict": "council_district",
            "exemptionValue": "exemption_value",
            "gisSequenceNumber": "gis_sequence_number",
            "improvedValue": "improved_value",
            "isPrimary": "is_primary",
            "landValue": "land_value",
            "legalDescription": "legal_description",
            "lot": "lot",
            "mapNumber": "map_number",
            "mapReferenceInfo": "map_reference_info",
            "page": "page",
            "parcel": "parcel",
            "parcelArea": "parcel_area",
            "parcelNumber": "parcel_number",
            "planArea": "plan_area",
            "range": "range",
            "section": "section",
            "supervisorDistrict": "supervisor_district",
            "township": "township",
            "tract": "tract",
            "status": "status",
            "subdivision": "subdivision",
            "owners": "owners",
            "recordId": "record_id",
        }

        for json_field, python_field in field_mapping.items():
            if json_field in data:
                fields[python_field] = data.get(json_field)

        return cls(**fields)


class RecordParcels(BaseResource):
    """Resource for interacting with Accela record parcels."""

    def list(
        self,
        record_id: str,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> ListResponse[RecordParcel]:
        """
        List all parcels associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get parcels for
            fields: List of fields to include in the response
            limit: Number of parcels per page, default 100
            offset: Starting offset for pagination, default 0

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/parcels"
        params = {"limit": limit, "offset": offset}

        if fields is not None and len(fields) > 0:
            params["fields"] = ",".join(fields)

        return self._list_resource(url, RecordParcel, params)

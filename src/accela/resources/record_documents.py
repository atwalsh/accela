from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordDocument(ResourceModel):
    """Represents a document associated with an Accela record."""

    id: int
    source: str
    file_name: str
    file_key: str
    entity_type: str
    entity_id: str
    service_provider_code: str
    department: str
    uploaded_by: str
    modified_by: str
    modified_date: datetime
    uploaded_date: datetime
    status_date: datetime
    type: str
    size: float
    description: Optional[str] = None
    category: Optional[Dict[str, str]] = None
    status: Optional[Dict[str, str]] = None
    group: Optional[Dict[str, str]] = None

    # Original JSON response
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "RecordDocument":
        """Create a RecordDocument instance from API response data."""

        # Parse date fields
        modified_date = datetime.strptime(data["modifiedDate"], "%Y-%m-%d %H:%M:%S")
        uploaded_date = datetime.strptime(data["uploadedDate"], "%Y-%m-%d %H:%M:%S")
        status_date = datetime.strptime(data["statusDate"], "%Y-%m-%d %H:%M:%S")

        # Handle nested objects
        category = (
            data.get("category") if isinstance(data.get("category"), dict) else None
        )
        status = data.get("status") if isinstance(data.get("status"), dict) else None
        group = data.get("group") if isinstance(data.get("group"), dict) else None

        return cls(
            id=data["id"],
            source=data["source"],
            file_name=data["fileName"],
            file_key=data["fileKey"],
            entity_type=data["entityType"],
            entity_id=data["entityId"],
            service_provider_code=data["serviceProviderCode"],
            department=data["department"],
            uploaded_by=data["uploadedBy"],
            modified_by=data["modifiedBy"],
            modified_date=modified_date,
            uploaded_date=uploaded_date,
            status_date=status_date,
            type=data["type"],
            size=data["size"],
            description=data.get("description"),
            category=category,
            status=status,
            group=group,
            raw_json=data,
        )


class RecordDocuments(BaseResource):
    """Resource for interacting with Accela record documents."""

    def list(
        self,
        record_id: str,
        limit: int = 100,
        offset: int = 0,
    ) -> ListResponse[RecordDocument]:
        """
        List all documents associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get documents for
            limit: Number of documents per page, default 100
            offset: Starting offset for pagination, default 0

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/documents"
        params = {"limit": limit, "offset": offset}

        return self._list_resource(url, RecordDocument, params)

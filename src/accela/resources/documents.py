from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional

import requests

from .base import BaseResource, ResourceModel


@dataclass
class Document(ResourceModel):
    """Represents a document from the Accela documents API."""

    id: str
    source: str
    file_name: str
    file_key: str
    entity_type: str
    entity_id: str
    service_provider_code: str
    uploaded_by: str
    modified_by: str
    modified_date: datetime
    uploaded_date: datetime
    status_date: datetime
    type: str
    size: float
    department: Optional[str] = None
    description: Optional[str] = None
    category: Optional[Dict[str, str]] = None
    status: Optional[Dict[str, str]] = None
    group: Optional[Dict[str, str]] = None

    # Original JSON response
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "Document":
        """Create a Document instance from API response data."""

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
            id=str(data["id"]),
            source=data["source"],
            file_name=data["fileName"],
            file_key=data["fileKey"],
            entity_type=data["entityType"],
            entity_id=data["entityId"],
            service_provider_code=data["serviceProviderCode"],
            department=data.get("department"),
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


class Documents(BaseResource):
    """Resource for interacting with Accela documents."""

    def retrieve(self, document_id: str) -> Document:
        """
        Retrieve a specific document by ID.

        Args:
            document_id: The ID of the document to retrieve

        Returns:
            Document object
        """
        url = f"{self.client.BASE_URL}/documents/{document_id}"
        result = self._get(url)
        return Document.from_json(result["result"][0])

    def download(self, document_id: str) -> requests.Response:
        """
        Download a document's binary content.

        Args:
            document_id: The ID of the document to download

        Returns:
            requests.Response object with binary content.
            Use response.iter_content() for streaming or response.content for full content.

        Example:
            response = client.documents.download("12345")
            with open("document.pdf", "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        """
        url = f"{self.client.BASE_URL}/documents/{document_id}/download"
        return self._get_binary(url)

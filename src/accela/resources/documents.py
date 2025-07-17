from dataclasses import dataclass, field
from typing import Any, Dict, Optional

import requests

from .base import BaseResource, ResourceModel


@dataclass
class Document(ResourceModel):
    """Represents a document from the Accela documents API."""

    category: Optional[Dict[str, Any]] = None
    deletable: Optional[Dict[str, Any]] = None
    department: Optional[str] = None
    description: Optional[str] = None
    downloadable: Optional[Dict[str, Any]] = None
    entity_id: Optional[str] = None
    entity_type: Optional[str] = None
    file_name: Optional[str] = None
    group: Optional[Dict[str, Any]] = None
    id: Optional[int] = None
    modified_by: Optional[str] = None
    modified_date: Optional[str] = None
    service_provider_code: Optional[str] = None
    size: Optional[int] = None
    source: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    status_date: Optional[str] = None
    title_viewable: Optional[Dict[str, Any]] = None
    type: Optional[str] = None
    uploaded_by: Optional[str] = None
    uploaded_date: Optional[str] = None
    virtual_folders: Optional[str] = None
    raw_json: Dict[str, Any] = field(default_factory=dict)

    FIELD_MAPPING = {
        "category": "category",
        "deletable": "deletable",
        "department": "department",
        "description": "description",
        "downloadable": "downloadable",
        "entityId": "entity_id",
        "entityType": "entity_type",
        "fileName": "file_name",
        "group": "group",
        "id": "id",
        "modifiedBy": "modified_by",
        "modifiedDate": "modified_date",
        "serviceProviderCode": "service_provider_code",
        "size": "size",
        "source": "source",
        "status": "status",
        "statusDate": "status_date",
        "titleViewable": "title_viewable",
        "type": "type",
        "uploadedBy": "uploaded_by",
        "uploadedDate": "uploaded_date",
        "virtualFolders": "virtual_folders",
    }

    JSON_FIELDS = [
        "category",
        "deletable",
        "downloadable",
        "group",
        "status",
        "titleViewable",
    ]


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

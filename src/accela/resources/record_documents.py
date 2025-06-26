from .base import BaseResource, ListResponse
from .documents import Document


class RecordDocuments(BaseResource):
    """Resource for interacting with Accela record documents."""

    def list(
        self,
        record_id: str,
        limit: int = 100,
        offset: int = 0,
    ) -> ListResponse[Document]:
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

        return self._list_resource(url, Document, params)

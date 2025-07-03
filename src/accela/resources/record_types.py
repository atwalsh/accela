from dataclasses import dataclass, field
from typing import Any, Dict

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordType(ResourceModel):
    """Represents an Accela record type."""

    value: str
    type: str
    text: str
    group: str
    subType: str
    category: str
    module: str
    alias: str
    id: str
    readable: bool
    createable: bool
    updatable: bool
    deletable: bool
    asChildOnly: str
    searchable: bool
    smartChoiceCode: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "RecordType":
        """Create a RecordType instance from API response data."""
        return cls(
            value=data["value"],
            type=data["type"],
            text=data["text"],
            group=data["group"],
            subType=data["subType"],
            category=data["category"],
            module=data["module"],
            alias=data["alias"],
            id=data["id"],
            readable=data["readable"],
            createable=data["createable"],
            updatable=data["updatable"],
            deletable=data["deletable"],
            asChildOnly=data["asChildOnly"],
            searchable=data["searchable"],
            smartChoiceCode=data["smartChoiceCode"],
            raw_json=data,
        )


class RecordTypes(BaseResource):
    """Record types resource for interacting with Accela settings/records/types API."""

    def list(
        self, *, module: str, limit: int = 100, offset: int = 0
    ) -> ListResponse[RecordType]:
        """
        List record types for a specific module with pagination support.

        Args:
            module: Module name to filter record types (required)
            limit: Number of record types per page, default 100
            offset: Starting offset for pagination, default 0

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/settings/records/types"
        params = {"module": module, "limit": limit, "offset": offset}

        result = self._get(url, params=params)

        # Parse the results into model instances
        items = [RecordType.from_json(item) for item in result["result"]]

        # Extract pagination info from the page object
        page = result["page"]
        total = page["total"]
        has_more = page["hasmore"]

        return ListResponse(
            data=items,
            has_more=has_more,
            offset=offset,
            limit=limit,
            total=total,
            _client=self.client,
            _params=params,
            _url=url,
            _model_class=RecordType,
        )

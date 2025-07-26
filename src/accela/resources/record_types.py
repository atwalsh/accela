from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordType(ResourceModel):
    """Represents an Accela record type."""

    id: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    alias: Optional[str] = None
    as_child_only: Optional[str] = None
    associations: Optional[Dict[str, Any]] = None
    category: Optional[str] = None
    createable: Optional[bool] = None
    deletable: Optional[bool] = None
    filter_name: Optional[str] = None
    group: Optional[str] = None
    module: Optional[str] = None
    readable: Optional[bool] = None
    searchable: Optional[bool] = None
    sub_type: Optional[str] = None
    text: Optional[str] = None
    type: Optional[str] = None
    updatable: Optional[bool] = None
    value: Optional[str] = None

    # Field mapping: API field name -> Python field name
    FIELD_MAPPING = {
        "alias": "alias",
        "asChildOnly": "as_child_only",
        "associations": "associations",
        "category": "category",
        "createable": "createable",
        "deletable": "deletable",
        "filterName": "filter_name",
        "group": "group",
        "id": "id",
        "module": "module",
        "readable": "readable",
        "searchable": "searchable",
        "subType": "sub_type",
        "text": "text",
        "type": "type",
        "updatable": "updatable",
        "value": "value",
    }

    # Dictionary object fields that need recursive snake_case conversion
    DICT_FIELDS = [
        "associations",
    ]

    BOOL_FIELDS = [
        "createable",
        "deletable",
        "readable",
        "searchable",
        "updatable",
    ]


class RecordTypes(BaseResource):
    """Record types resource for interacting with Accela settings/records/types API."""

    def list(self, *, module: str, limit: int = 100, offset: int = 0) -> ListResponse[RecordType]:
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

        return self._list_resource(url, RecordType, params)

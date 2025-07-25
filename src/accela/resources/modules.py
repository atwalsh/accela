from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .base import BaseResource, ResourceModel


@dataclass
class Module(ResourceModel):
    """Represents an Accela module."""

    text: str
    value: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    address_types: Optional[List[Dict[str, Any]]] = None

    FIELD_MAPPING = {
        "addressTypes": "address_types",
        "text": "text",
        "value": "value",
    }

    DICT_FIELDS = [
        "addressTypes",
    ]


class Modules(BaseResource):
    """Modules resource for interacting with Accela settings/modules API."""

    def list(self) -> List[Module]:
        """
        List all available modules.

        Returns:
            List of Module objects
        """
        url = f"{self.client.BASE_URL}/settings/modules"
        result = self._get(url)
        return [Module.from_json(item, self.client) for item in result["result"]]

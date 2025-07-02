from dataclasses import dataclass, field
from typing import Any, Dict, List

from .base import BaseResource, ResourceModel


@dataclass
class Module(ResourceModel):
    """Represents an Accela module."""

    value: str
    text: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "Module":
        """Create a Module instance from API response data."""
        return cls(
            value=data["value"],
            text=data["text"],
            raw_json=data,
        )


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
        return [Module.from_json(item) for item in result["result"]]

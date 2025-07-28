from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class Agency(ResourceModel):
    """Represents an Accela agency."""

    name: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    country: Optional[str] = None
    display_name: Optional[str] = None
    enabled: Optional[bool] = None
    hosted_aca: Optional[bool] = None
    icon_name: Optional[str] = None
    is_for_demo: Optional[bool] = None
    service_provider_code: Optional[str] = None
    state: Optional[str] = None

    FIELD_MAPPING = {
        "country": "country",
        "displayName": "display_name",
        "enabled": "enabled",
        "hostedACA": "hosted_aca",
        "iconName": "icon_name",
        "isForDemo": "is_for_demo",
        "name": "name",
        "serviceProviderCode": "service_provider_code",
        "state": "state",
    }

    BOOL_FIELDS = ["enabled", "hostedACA", "isForDemo"]


class Agencies(BaseResource):
    """Resource for interacting with Accela agencies.
    
    This resource does not require agency or environment context.
    """

    # Override to allow global access
    REQUIRES_AGENCY = False
    REQUIRES_ENVIRONMENT = False

    def list(
            self,
            limit: int = 100,
            offset: int = 0,
            name: Optional[str] = None,
    ) -> ListResponse[Agency]:
        """List all enabled agencies.

        Args:
            limit: Maximum number of agencies to return (default: 100)
            offset: Number of agencies to skip (default: 0)
            name: Optional agency name filter

        Returns:
            ListResponse[Agency]: Paginated list of agencies
        """
        url = f"{self.client.BASE_URL}/agencies"
        params: Dict[str, Any] = {"limit": limit, "offset": offset}

        if name:
            params["name"] = name

        return self._list_resource(url, Agency, params)

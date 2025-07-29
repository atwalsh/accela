from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class AgencyEnvironment(ResourceModel):
    """Represents an Accela agency environment."""

    name: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    biz_server_url: Optional[str] = None
    biz_server_version: Optional[str] = None
    enabled: Optional[bool] = None
    gateway_version: Optional[str] = None
    host_environment_detail_models: Optional[List[Dict[str, Any]]] = None
    host_id: Optional[str] = None
    id: Optional[str] = None
    is_aa_biz_server: Optional[bool] = None
    is_azure_hosted: Optional[bool] = None
    is_default: Optional[bool] = None
    product: Optional[str] = None
    tenants: Optional[List[Dict[str, Any]]] = None
    version: Optional[str] = None

    FIELD_MAPPING = {
        "bizServerURL": "biz_server_url",
        "bizServerVersion": "biz_server_version",
        "enabled": "enabled",
        "gatewayVersion": "gateway_version",
        "hostEnvironmentDetailModels": "host_environment_detail_models",
        "hostId": "host_id",
        "id": "id",
        "isAABizServer": "is_aa_biz_server",
        "isAzureHosted": "is_azure_hosted",
        "isDefault": "is_default",
        "name": "name",
        "product": "product",
        "tenants": "tenants",
        "version": "version",
    }

    DICT_FIELDS = ["hostEnvironmentDetailModels", "tenants"]
    BOOL_FIELDS = ["enabled", "isAABizServer", "isAzureHosted", "isDefault"]


class AgencyEnvironments(BaseResource):
    """Resource for interacting with Accela agency environments.
    
    This resource does not require agency or environment context.
    """

    # Override to allow global access
    REQUIRES_AGENCY = False
    REQUIRES_ENVIRONMENT = False

    def list(self, name: str) -> ListResponse[AgencyEnvironment]:
        """List environments for a specific agency.

        Args:
            name: The agency name to get environments for

        Returns:
            ListResponse[AgencyEnvironment]: Paginated list of agency environments
        """
        url = f"{self.client.BASE_URL}/agencies/{name}/environments"
        params: Dict[str, Any] = {}

        return self._list_resource(url, AgencyEnvironment, params)

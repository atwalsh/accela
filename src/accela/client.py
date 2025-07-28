from typing import ClassVar, Dict, Optional, Type
from zoneinfo import ZoneInfo

from .resources.agencies import Agencies
from .resources.base import BaseResource
from .resources.documents import Documents
from .resources.modules import Modules
from .resources.record_addresses import RecordAddresses
from .resources.record_documents import RecordDocuments
from .resources.record_parcels import RecordParcels
from .resources.record_types import RecordTypes
from .resources.records import Records


class AccelaClient:
    """Main client for interacting with the Accela API."""

    BASE_URL = "https://apis.accela.com/v4"

    # Define resource classes to be automatically initialized
    RESOURCE_CLASSES: ClassVar[Dict[str, Type[BaseResource]]] = {
        "agencies": Agencies,
        "records": Records,
        "record_addresses": RecordAddresses,
        "record_documents": RecordDocuments,
        "record_parcels": RecordParcels,
        "documents": Documents,
        "modules": Modules,
        "record_types": RecordTypes,
    }

    # Hinting
    agencies: Agencies
    records: Records
    record_addresses: RecordAddresses
    record_documents: RecordDocuments
    record_parcels: RecordParcels
    documents: Documents
    modules: Modules
    record_types: RecordTypes

    def __init__(
            self,
            access_token: str,
            agency: Optional[str] = None,
            environment: Optional[str] = None,
            timezone: Optional[ZoneInfo] = None,
    ):
        """
        Initialize the Accela client.

        Args:
            access_token: Accela API access token
            agency: Optional agency name; e.g. 'CHARLOTTE'. Required for agency-specific resources.
            environment: Optional environment name; e.g. 'PROD'. Required for agency-specific resources.
            timezone: Optional timezone for converting naive datetime strings from API to timezone-aware datetimes
        """
        self.access_token = access_token
        self.agency = agency
        self.environment = environment
        self.timezone = timezone

        # Store resource classes for lazy initialization
        self._resource_instances = {}

    def __getattr__(self, name: str):
        """Lazy initialization of resources when accessed."""
        if name in self.RESOURCE_CLASSES:
            if name not in self._resource_instances:
                resource_class = self.RESOURCE_CLASSES[name]
                self._resource_instances[name] = resource_class(self)
            return self._resource_instances[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def register_resource(self, name: str, resource_class: Type[BaseResource]) -> None:
        """Register a new resource class with the client.

        Args:
            name: Attribute name to use for the resource
            resource_class: Resource class to instantiate
        """
        self.RESOURCE_CLASSES[name] = resource_class
        # Clear cached instance if it exists
        if name in self._resource_instances:
            del self._resource_instances[name]

    @property
    def headers(self) -> Dict[str, str]:
        """Default headers for Accela API requests."""
        headers = {
            "Authorization": self.access_token,
        }
        
        # Only include agency and environment headers if they are provided
        if self.agency:
            headers["x-accela-agency"] = self.agency
        if self.environment:
            headers["x-accela-environment"] = self.environment
            
        return headers

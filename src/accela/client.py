from typing import ClassVar, Dict, Optional, Type
from zoneinfo import ZoneInfo

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
        "records": Records,
        "record_addresses": RecordAddresses,
        "record_documents": RecordDocuments,
        "record_parcels": RecordParcels,
        "documents": Documents,
        "modules": Modules,
        "record_types": RecordTypes,
    }

    # Hinting
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
            agency: str,
            environment: str,
            timezone: Optional[ZoneInfo] = None,
    ):
        """
        Initialize the Accela client.

        Args:
            access_token: Accela API access token
            agency: Agency name; e.g. 'CHARLOTTE'
            environment: Environment name; e.g. 'PROD'
            timezone: Optional timezone for converting naive datetime strings from API to timezone-aware datetimes
        """
        self.access_token = access_token
        self.agency = agency
        self.environment = environment
        self.timezone = timezone

        # Initialize all resources
        self._init_resources()

    def _init_resources(self) -> None:
        """Initialize all resource classes."""
        for name, resource_class in self.RESOURCE_CLASSES.items():
            setattr(self, name, resource_class(self))

    def register_resource(self, name: str, resource_class: Type[BaseResource]) -> None:
        """Register a new resource class with the client.

        Args:
            name: Attribute name to use for the resource
            resource_class: Resource class to instantiate
        """
        self.RESOURCE_CLASSES[name] = resource_class
        setattr(self, name, resource_class(self))

    @property
    def headers(self) -> Dict[str, str]:
        """Default headers for Accela API requests."""
        return {
            "Authorization": self.access_token,
            "x-accela-agency": self.agency,
            "x-accela-environment": self.environment,
        }

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Dict, List, Optional

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class Record(ResourceModel):
    """Represents an Accela record."""

    actual_production_unit: Optional[float] = None
    addresses: Optional[List[Dict[str, Any]]] = None
    appearance_date: Optional[str] = None
    appearance_day_of_week: Optional[str] = None
    assets: Optional[List[Dict[str, Any]]] = None
    assigned_date: Optional[str] = None
    assigned_to_department: Optional[str] = None
    assigned_user: Optional[str] = None
    balance: Optional[float] = None
    booking: Optional[bool] = None
    closed_by_department: Optional[str] = None
    closed_by_user: Optional[str] = None
    closed_date: Optional[str] = None
    complete_date: Optional[str] = None
    completed_by_department: Optional[str] = None
    completed_by_user: Optional[str] = None
    condition_of_approvals: Optional[List[Dict[str, Any]]] = None
    conditions: Optional[List[Dict[str, Any]]] = None
    construction_type: Optional[Dict[str, Any]] = None
    contact: Optional[List[Dict[str, Any]]] = None
    cost_per_unit: Optional[float] = None
    created_by: Optional[str] = None
    created_by_cloning: Optional[str] = None
    custom_forms: Optional[List[Dict[str, Any]]] = None
    custom_id: Optional[str] = None
    custom_tables: Optional[List[Dict[str, Any]]] = None
    defendant_signature: Optional[bool] = None
    description: Optional[str] = None
    enforce_department: Optional[str] = None
    enforce_user: Optional[str] = None
    enforce_user_id: Optional[str] = None
    estimated_cost_per_unit: Optional[float] = None
    estimated_due_date: Optional[str] = None
    estimated_production_unit: Optional[float] = None
    estimated_total_job_cost: Optional[float] = None
    first_issued_date: Optional[str] = None
    housing_units: Optional[int] = None
    id: Optional[str] = None
    in_possession_time: Optional[float] = None
    infraction: Optional[bool] = None
    initiated_product: Optional[str] = None
    inspector_department: Optional[str] = None
    inspector_id: Optional[str] = None
    inspector_name: Optional[str] = None
    job_value: Optional[float] = None
    misdemeanor: Optional[bool] = None
    module: Optional[str] = None
    name: Optional[str] = None
    number_of_buildings: Optional[int] = None
    offense_witnessed: Optional[bool] = None
    opened_date: Optional[str] = None
    overall_application_time: Optional[float] = None
    owner: Optional[List[Dict[str, Any]]] = None
    parcel: Optional[List[Dict[str, Any]]] = None
    priority: Optional[Dict[str, Any]] = None
    professional: Optional[List[Dict[str, Any]]] = None
    public_owned: Optional[bool] = None
    record_class: Optional[str] = None
    renewal_info: Optional[Dict[str, Any]] = None
    reported_channel: Optional[Dict[str, Any]] = None
    reported_date: Optional[str] = None
    reported_type: Optional[Dict[str, Any]] = None
    scheduled_date: Optional[str] = None
    severity: Optional[Dict[str, Any]] = None
    short_notes: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    status_date: Optional[str] = None
    status_reason: Optional[Dict[str, Any]] = None
    status_type: Optional[str] = None
    total_fee: Optional[float] = None
    total_job_cost: Optional[float] = None
    total_pay: Optional[float] = None
    tracking_id: Optional[int] = None
    type: Optional[Dict[str, Any]] = None
    undistributed_cost: Optional[float] = None
    update_date: Optional[str] = None
    value: Optional[str] = None
    raw_json: Dict[str, Any] = field(default_factory=dict)

    # Field mapping: API field name -> Python field name
    FIELD_MAPPING = {
        "actualProductionUnit": "actual_production_unit",
        "addresses": "addresses",
        "appearanceDate": "appearance_date",
        "appearanceDayOfWeek": "appearance_day_of_week",
        "assets": "assets",
        "assignedDate": "assigned_date",
        "assignedToDepartment": "assigned_to_department",
        "assignedUser": "assigned_user",
        "balance": "balance",
        "booking": "booking",
        "closedByDepartment": "closed_by_department",
        "closedByUser": "closed_by_user",
        "closedDate": "closed_date",
        "completeDate": "complete_date",
        "completedByDepartment": "completed_by_department",
        "completedByUser": "completed_by_user",
        "conditionOfApprovals": "condition_of_approvals",
        "conditions": "conditions",
        "constructionType": "construction_type",
        "contact": "contact",
        "costPerUnit": "cost_per_unit",
        "createdBy": "created_by",
        "createdByCloning": "created_by_cloning",
        "customForms": "custom_forms",
        "customId": "custom_id",
        "customTables": "custom_tables",
        "defendantSignature": "defendant_signature",
        "description": "description",
        "enforceDepartment": "enforce_department",
        "enforceUser": "enforce_user",
        "enforceUserId": "enforce_user_id",
        "estimatedCostPerUnit": "estimated_cost_per_unit",
        "estimatedDueDate": "estimated_due_date",
        "estimatedProductionUnit": "estimated_production_unit",
        "estimatedTotalJobCost": "estimated_total_job_cost",
        "firstIssuedDate": "first_issued_date",
        "housingUnits": "housing_units",
        "id": "id",
        "inPossessionTime": "in_possession_time",
        "infraction": "infraction",
        "initiatedProduct": "initiated_product",
        "inspectorDepartment": "inspector_department",
        "inspectorId": "inspector_id",
        "inspectorName": "inspector_name",
        "jobValue": "job_value",
        "misdemeanor": "misdemeanor",
        "module": "module",
        "name": "name",
        "numberOfBuildings": "number_of_buildings",
        "offenseWitnessed": "offense_witnessed",
        "openedDate": "opened_date",
        "overallApplicationTime": "overall_application_time",
        "owner": "owner",
        "parcel": "parcel",
        "priority": "priority",
        "professional": "professional",
        "publicOwned": "public_owned",
        "recordClass": "record_class",
        "renewalInfo": "renewal_info",
        "reportedChannel": "reported_channel",
        "reportedDate": "reported_date",
        "reportedType": "reported_type",
        "scheduledDate": "scheduled_date",
        "severity": "severity",
        "shortNotes": "short_notes",
        "status": "status",
        "statusDate": "status_date",
        "statusReason": "status_reason",
        "statusType": "status_type",
        "totalFee": "total_fee",
        "totalJobCost": "total_job_cost",
        "totalPay": "total_pay",
        "trackingId": "tracking_id",
        "type": "type",
        "undistributedCost": "undistributed_cost",
        "updateDate": "update_date",
        "value": "value",
    }

    # JSON object fields that need recursive snake_case conversion
    JSON_FIELDS = [
        "addresses",
        "assets",
        "conditionOfApprovals",
        "conditions",
        "constructionType",
        "contact",
        "customForms",
        "customTables",
        "owner",
        "parcel",
        "priority",
        "professional",
        "renewalInfo",
        "reportedChannel",
        "reportedType",
        "severity",
        "status",
        "statusReason",
        "type",
    ]


class Records(BaseResource):
    """Records resource for interacting with Accela records API."""

    def list(
            self,
            limit: int = 100,
            offset: int = 0,
            module: str = None,
            record_type: str = None,
            opened_date_after: date = None,
    ) -> ListResponse[Record]:
        """
        List records with pagination support.

        Args:
            limit: Number of records per page, default 100
            offset: Starting offset for pagination, default 0
            module: Filter records by module name
            record_type: Filter records by record type
            opened_date_after: Filter records opened on or after this date

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/records"
        params = {"limit": limit, "offset": offset}

        # Add filters if provided
        if module:
            params["module"] = module

        if record_type:
            params["type"] = record_type

        if opened_date_after:
            # Format date as YYYY-MM-DD for the API
            params["openedDateFrom"] = opened_date_after.strftime("%Y-%m-%d")

        # Use the generic list method from BaseResource
        return self._list_resource(url, Record, params)

    def retrieve(self, record_id: str) -> Record:
        """
        Retrieve a specific record by ID.

        Args:
            record_id: The ID of the record to retrieve

        Returns:
            Record object
        """
        url = f"{self.client.BASE_URL}/records/{record_id}"
        result = self._get(url)
        return Record.from_json(result["result"][0])

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, Dict, List, Optional, Union

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class Record(ResourceModel):
    """Represents an Accela record."""

    id: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    actual_production_unit: Optional[float] = None
    addresses: Optional[List[Dict[str, Any]]] = None
    appearance_date: Optional[datetime] = None
    appearance_day_of_week: Optional[str] = None
    assets: Optional[List[Dict[str, Any]]] = None
    assigned_date: Optional[datetime] = None
    assigned_to_department: Optional[str] = None
    assigned_user: Optional[str] = None
    balance: Optional[float] = None
    booking: Optional[bool] = None
    closed_by_department: Optional[str] = None
    closed_by_user: Optional[str] = None
    closed_date: Optional[datetime] = None
    complete_date: Optional[datetime] = None
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
    estimated_due_date: Optional[datetime] = None
    estimated_production_unit: Optional[float] = None
    estimated_total_job_cost: Optional[float] = None
    first_issued_date: Optional[datetime] = None
    housing_units: Optional[int] = None
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
    opened_date: Optional[datetime] = None
    overall_application_time: Optional[float] = None
    owner: Optional[List[Dict[str, Any]]] = None
    parcel: Optional[List[Dict[str, Any]]] = None
    priority: Optional[Dict[str, Any]] = None
    professional: Optional[List[Dict[str, Any]]] = None
    public_owned: Optional[bool] = None
    record_class: Optional[str] = None
    renewal_info: Optional[Dict[str, Any]] = None
    reported_channel: Optional[Dict[str, Any]] = None
    reported_date: Optional[datetime] = None
    reported_type: Optional[Dict[str, Any]] = None
    scheduled_date: Optional[datetime] = None
    severity: Optional[Dict[str, Any]] = None
    short_notes: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    status_date: Optional[datetime] = None
    status_reason: Optional[Dict[str, Any]] = None
    status_type: Optional[str] = None
    total_fee: Optional[float] = None
    total_job_cost: Optional[float] = None
    total_pay: Optional[float] = None
    tracking_id: Optional[int] = None
    type: Optional[Dict[str, Any]] = None
    undistributed_cost: Optional[float] = None
    update_date: Optional[datetime] = None
    value: Optional[str] = None

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

    DICT_FIELDS = [
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

    DATETIME_FIELDS = [
        "appearanceDate",
        "assignedDate",
        "closedDate",
        "completeDate",
        "estimatedDueDate",
        "firstIssuedDate",
        "openedDate",
        "reportedDate",
        "scheduledDate",
        "statusDate",
        "updateDate",
    ]

    BOOL_FIELDS = [
        "booking",
        "defendantSignature",
        "infraction",
        "misdemeanor",
        "offenseWitnessed",
        "publicOwned",
    ]


class Records(BaseResource):
    """Records resource for interacting with Accela records API."""

    def list(
            self,
            limit: int = 100,
            offset: int = 0,
            type: Optional[str] = None,  # noqa
            opened_date_from: Optional[Union[date, datetime]] = None,
            opened_date_to: Optional[Union[date, datetime]] = None,
            custom_id: Optional[str] = None,
            module: Optional[str] = None,
            status: Optional[str] = None,
            assigned_to_department: Optional[str] = None,
            assigned_user: Optional[str] = None,
            assigned_date_from: Optional[Union[date, datetime]] = None,
            assigned_date_to: Optional[Union[date, datetime]] = None,
            completed_date_from: Optional[Union[date, datetime]] = None,
            completed_date_to: Optional[Union[date, datetime]] = None,
            status_date_from: Optional[Union[date, datetime]] = None,
            status_date_to: Optional[Union[date, datetime]] = None,
            completed_by_department: Optional[str] = None,
            completed_by_user: Optional[str] = None,
            closed_date_from: Optional[Union[date, datetime]] = None,
            closed_date_to: Optional[Union[date, datetime]] = None,
            closed_by_department: Optional[str] = None,
            closed_by_user: Optional[str] = None,
            record_class: Optional[str] = None,
    ) -> ListResponse[Record]:
        """
        List records with pagination support and various filters.

        Args:
            limit: Number of records per page, default 100
            offset: Starting offset for pagination, default 0
            type: Filter by record type
            opened_date_from: Filter by the record's open date range, beginning with this date/datetime
            opened_date_to: Filter by the record's open date range, ending with this date/datetime
            custom_id: Filter by the record custom id
            module: Filter by module
            status: Filter by record status
            assigned_to_department: Filter by the assigned department
            assigned_user: Filter by the assigned user
            assigned_date_from: Filter by the record's assigned date range starting with this date/datetime
            assigned_date_to: Filter by the record's assigned date range ending with this date/datetime
            completed_date_from: Filter by the record's completed date range starting with this date/datetime
            completed_date_to: Filter by the record's completed date range ending with this date/datetime
            status_date_from: Filter by the record's status date range starting with this date/datetime
            status_date_to: Filter by the record's status date range ending with this date/datetime
            completed_by_department: Filter by the department which completed the application
            completed_by_user: Filter by the user who completed the application
            closed_date_from: Filter by the record's closed date range starting with this date/datetime
            closed_date_to: Filter by the record's closed date range ending with this date/datetime
            closed_by_department: Filter by the department which closed the application
            closed_by_user: Filter by the user who closed the application
            record_class: Filter by record class

        Returns:
            ListResponse object with pagination support
        """
        url = f"{self.client.BASE_URL}/records"
        params: Dict[str, Any] = {"limit": limit, "offset": offset}

        def format_date_param(date_param):
            if date_param is None:
                return None

            # Convert date to datetime if needed
            if isinstance(date_param, date) and not isinstance(date_param, datetime):
                # Convert date to datetime at start of day
                date_param = datetime.combine(date_param, datetime.min.time())

            # If datetime is timezone-naive and client has timezone, make it timezone-aware
            if isinstance(date_param, datetime) and date_param.tzinfo is None and self.client.timezone:
                date_param = date_param.replace(tzinfo=self.client.timezone)

            return date_param.isoformat()

        filter_params = {
            "type": type,
            "openedDateFrom": format_date_param(opened_date_from),
            "openedDateTo": format_date_param(opened_date_to),
            "customId": custom_id,
            "module": module,
            "status": status,
            "assignedToDepartment": assigned_to_department,
            "assignedUser": assigned_user,
            "assignedDateFrom": format_date_param(assigned_date_from),
            "assignedDateTo": format_date_param(assigned_date_to),
            "completedDateFrom": format_date_param(completed_date_from),
            "completedDateTo": format_date_param(completed_date_to),
            "statusDateFrom": format_date_param(status_date_from),
            "statusDateTo": format_date_param(status_date_to),
            "completedByDepartment": completed_by_department,
            "completedByUser": completed_by_user,
            "closedDateFrom": format_date_param(closed_date_from),
            "closedDateTo": format_date_param(closed_date_to),
            "closedByDepartment": closed_by_department,
            "closedByUser": closed_by_user,
            "recordClass": record_class,
        }

        for key, value in filter_params.items():
            if value is not None:
                params[key] = value

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
        return Record.from_json(result["result"][0], self.client)

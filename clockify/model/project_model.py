from typing import Optional, List
from typing_extensions import Literal

from clockify.model.base_model import BaseModel
from pydantic import ConfigDict


class HourlyRate(BaseModel):
    amount: Optional[str] = None
    currency: Optional[str] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={"ammount": "amount", "amount": "amount"})


class MemberShip(BaseModel):
    user_Id: Optional[str] = None
    hourly_rate: Optional[str] = None
    cost_rate: Optional[str] = None
    target_Id: Optional[str] = None
    membership_Type: Optional[str] = None
    membership_Status: Optional[str] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "user_Id": "userId",
        "hourly_rate": "hourlyRate",
        "cost_rate": "costRate",
        "target_Id": "targetId",
        "membership_Type": "membershipType",
        "membership_Status": "membershipStatus",
    })


class Estimate(BaseModel):
    estimate: Optional[str] = None
    type: Optional[str] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={"estimate": "estimate", "type": "type"})


class TimeEstimate(BaseModel):
    estimate: Optional[str] = None
    type: Optional[str] = None
    reset_option: Optional[str] = None
    active: Optional[bool] = None
    include_non_billable: Optional[bool] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "estimate": "estimate",
        "type": "type",
        "reset_option": "resetOption",
        "active": "active",
        "include_non_billable": "includeNonBillable",
    })


class Project(BaseModel):
    name: str
    workspace_id: str
    id_: Optional[str] = None
    hourly_rate: Optional[HourlyRate] = None
    client_id: Optional[str] = None
    billable: Optional[bool] = None
    memberships: Optional[List[MemberShip]] = None
    color: Optional[str] = None
    estimate: Optional[Estimate] = None
    archived: Optional[bool] = None
    duration: Optional[str] = None
    client_name: Optional[str] = None
    note: Optional[str] = None
    cost_rate: Optional[str] = None
    time_estimate: Optional[TimeEstimate] = None
    budget_estimate: Optional[str] = None
    template: Optional[bool] = None
    public_: Optional[bool] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "id_": "id",
        "name": "name",
        "hourly_rate": "hourlyRate",
        "client_id": "clientId",
        "workspace_id": "workspaceId",
        "billable": "billable",
        "memberships": "memberships",
        "color": "color",
        "estimate": "estimate",
        "archived": "archived",
        "duration": "duration",
        "client_name": "clientName",
        "note": "note",
        "cost_rate": "costRate",
        "time_estimate": "timeEstimate",
        "budget_estimate": "budgetEstimate",
        "template": "template",
        "public_": "public",
    })


class ProjectGetParams(BaseModel):
    hydrated: Optional[bool] = None
    archived: Optional[bool] = None
    name: Optional[str] = None
    page: int = 1
    page_size: int = 50
    billable: Optional[bool] = None
    clients: Optional[List[str]] = None
    contains_client: Optional[bool] = None
    client_status: Optional[Literal["ACTIVE", "ARCHIVED"]] = None
    users: Optional[List[str]] = None
    contains_users: Optional[bool] = None
    user_status: Optional[Literal["ACTIVE", "ARCHIVED"]] = None
    is_template: Optional[bool] = None
    sort_column: Optional[Literal["NAME", "CLIENT_NAME", "DURATION"]] = None
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "page_size": "page-size",
        "contains_client": "contains-client",
        "client_status": "client-status",
        "contains_users": "contains-users",
        "user_status": "user-status",
        "is_template": "is-template",
        "sort_column": "sort-column",
        "sort_order": "sort-order",
    })

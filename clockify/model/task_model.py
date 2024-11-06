from typing import List, Optional
from typing_extensions import Literal

from clockify.model.base_model import BaseModel
from pydantic import ConfigDict


class CostRate_HourlyRate(BaseModel):
    amount: int
    currency: str


class Task(BaseModel):
    id_: str = None
    name: str
    project_id: str
    assignee_ids: List[str] = []
    estimate: str = None
    billable: bool = None
    hourly_rate: CostRate_HourlyRate = None
    cost_rate: CostRate_HourlyRate = None
    status: Literal["ACTIVE", "Done"] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "id_": "id",
        "project_id": "projectId",
        "assignee_ids": "assigneIds",
        "hourly_rate": "hourlyRate",
        "cost_rate": "costRate",
    })


class TaskGetParams(BaseModel):
    is_active: Optional[bool] = None
    name: Optional[str] = None
    page: int = 1
    page_size: int = 50
    strict_name_search: Optional[bool] = None
    sort_column: Optional[Literal["ID", "NAME"]] = None
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "is_active": "is-active",
        "page_size": "page-size",
        "strict_name_search": "strict-name-search",
        "sort_column": "sort-column",
        "sort_order": "sort-order",
    })

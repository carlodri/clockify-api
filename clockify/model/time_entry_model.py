from datetime import datetime
from typing import Any, List, Optional

from clockify.model.base_model import BaseModel
from clockify.model.user_model import User
from clockify.model.tag_model import Tag
from clockify.model.task_model import Task
from clockify.model.project_model import Project
from pydantic import ConfigDict


class TimeInterval(BaseModel):
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[str] = None


class HourlyRate(BaseModel):
    amount: Optional[float] = None
    currency: Optional[str] = None


class TimeEntry(BaseModel):
    id_: Optional[str] = None
    description: str
    tags: Optional[List[Tag]] = None
    tag_ids: Optional[List[str]] = None
    user: Optional[User] = None
    user_id: Optional[str] = None
    billable: Optional[bool] = None
    task: Optional[Task] = None
    task_id: Optional[str] = None
    project: Optional[Project] = None
    project_id: Optional[str] = None
    time_interval: Optional[TimeInterval] = None
    workspace_id: Optional[str] = None
    hourly_rate: Optional[HourlyRate] = None
    custom_field_values: List[Any]
    is_locked: Optional[bool] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "id_": "id",
        "tag_ids": "tagIds",
        "user_id": "userId",
        "task_id": "taskId",
        "project_id": "projectId",
        "time_interval": "timeInterval",
        "workspace_id": "workspaceId",
        "hourly_rate": "hourlyRate",
        "custom_field_values": "customFieldValues",
        "is_locked": "isLocked",
    })


class TimeEntryGetParams(BaseModel):
    description: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    project: Optional[str] = None
    task: Optional[str] = None
    tags: Optional[List[str]] = None
    project_required: Optional[bool] = None
    task_required: Optional[bool] = None
    hydrated: Optional[bool] = None
    in_progress: Optional[bool] = None
    page: Optional[int] = 1
    page_size: Optional[int] = 50


class CreateTimeEntryDTO(BaseModel):
    start: datetime
    end: datetime
    billable: bool = True
    description: str
    project_id: Optional[str] = None
    task_id: Optional[str] = None
    tag_ids: Optional[List[str]] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={"project_id": "projectId", "task_id": "taskId", "tag_ids": "tagIds"})

from typing import List, Optional
from typing_extensions import Literal

from clockify.model.base_model import BaseModel
from pydantic import ConfigDict


class Membership(BaseModel):
    user_id: Optional[str] = None
    hourly_rate: Optional[float] = None
    cost_rate: Optional[float] = None
    target_id: Optional[str] = None
    membership_type: Optional[str] = None
    membership_status: Optional[str] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "user_id": "userId",
        "hourly_rate": "hourlyRate",
        "cost_rate": "costRate",
        "target_id": "targetId",
        "membership_type": "membershipType",
        "membership_status": "membershipStatus",
    })


class SummaryReportSettings(BaseModel):
    group: Optional[str] = None
    subgroup: Optional[str] = None


class Settings(BaseModel):
    week_start: Optional[
        Literal[
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ] = None
    time_zone: Optional[str] = None
    time_format: Optional[str] = None
    date_format: Optional[str] = None
    send_newsletter: Optional[str] = None
    weekly_updates: Optional[str] = None
    long_running: Optional[str] = None
    scheduled_reports: Optional[str] = None
    approval: Optional[str] = None
    pto: Optional[str] = None
    alerts: Optional[str] = None
    reminders: Optional[str] = None
    time_tracking_manual: Optional[str] = None
    summary_report_settings: Optional[SummaryReportSettings] = None
    is_compact_view_on: Optional[str] = None
    dashboard_selection: Optional[str] = None
    dashboard_view_type: Optional[str] = None
    dashboard_pin_to_top: Optional[str] = None
    project_list_collapse: Optional[str] = None
    collapse_all_project_lists: Optional[str] = None
    group_similar_entries_disabled: Optional[str] = None
    my_start_of_day: Optional[str] = None
    project_picker_task_filter: Optional[str] = None
    lang: Optional[str] = None
    multi_factor_enabled: Optional[str] = None
    theme: Optional[str] = None
    scheduling: Optional[str] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "week_start": "weekStart",
        "time_zone": "timeZone",
        "time_format": "timeFormat",
        "date_format": "dateFormat",
        "send_newsletter": "sendNewsletter",
        "weekly_updates": "weeklyUpdates",
        "long_running": "longRunning",
        "scheduled_reports": "scheduledReports",
        "approval": "approval",
        "pto": "pto",
        "alerts": "alerts",
        "reminders": "reminders",
        "time_tracking_manual": "timeTrackingManual",
        "summary_report_settings": "summaryReportSettings",
        "is_compact_view_on": "isCompactViewOn",
        "dashboard_selection": "dashboardSelection",
        "dashboard_view_type": "dashboardViewType",
        "dashboard_pin_to_top": "dashboardPinToTop",
        "project_list_collapse": "projectListCollapse",
        "collapse_all_project_lists": "collapseAllProjectLists",
        "group_similar_entries_disabled": "groupSimilarEntriesDisabled",
        "my_start_of_day": "myStartOfDay",
        "project_picker_task_filter": "projectPickerTaskFilter",
        "lang": "lang",
        "multi_factor_enabled": "multiFactorEnabled",
        "theme": "theme",
        "scheduling": "scheduling",
    })


class User(BaseModel):
    id_: Optional[str] = None
    email: Optional[str] = None
    name: str
    memberships: Optional[List[Membership]] = None
    profile_picture: Optional[str] = None
    active_workspace: Optional[str] = None
    default_workspace: Optional[str] = None
    settings: Optional[Settings] = None
    status: Optional[str] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "id_": "id",
        "email": "email",
        "name": "name",
        "memberships": "memberships",
        "profile_picture": "profilePicture",
        "active_workspace": "activeWorkspace",
        "default_workspace": "defaultWorkspace",
        "settings": "settings",
        "status": "status",
    })

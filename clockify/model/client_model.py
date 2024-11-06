from typing_extensions import Literal

from clockify.model.base_model import BaseModel
from pydantic import ConfigDict


class Client(BaseModel):
    id_: str = None
    name: str
    workspace_id: str
    archived: bool = False
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={"id_": "id", "workspace_id": "workspaceId"})


class ClientGetParams(BaseModel):
    archived: bool = None
    name: str = None
    page: int = 1
    page_size: int = 50
    sort_column: Literal["NAME"] = None
    sort_order: Literal["ASCENDING", "DESCENDING"] = None
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={
        "page_size": "page-size",
        "sort_column": "sort-column",
        "sort_order": "sort-order",
    })


class ClientUpdateParams(BaseModel):
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={"archive_projects": "archive-projects"})

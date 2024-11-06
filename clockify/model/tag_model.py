from typing import Optional

from clockify.model.base_model import BaseModel
from pydantic import ConfigDict


class Tag(BaseModel):
    id_: str = None
    name: str
    workspace_id: str
    archived: bool = False
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={"id_": "id", "workspace_id": "workspaceId"})


class TagGetParams(BaseModel):
    name: Optional[str] = None
    archived: Optional[bool] = None
    page: int = 1
    page_size: int = 50
    # TODO[pydantic]: The following keys were removed: `fields`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(fields={"page_size": "page-size"})

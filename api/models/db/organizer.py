from pydantic import BaseModel
from uuid import UUID

from api.models.enums import CommunityType


class Organizer(BaseModel):
    id: UUID
    type: CommunityType
    name: str
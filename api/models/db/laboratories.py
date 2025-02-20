from pydantic import BaseModel
from uuid import UUID


class Laboratories(BaseModel):
    id: UUID
    batch_size: int
    name_of_equipment: list[str]
    safety_measures: list[str]
    weekly_utilization: int
    technical_manpower_ids: list[UUID]

    def to_dict(self):
        return {
            "id": str(self.id),
            "batch_size": self.batch_size,
            "name_of_equipment": self.name_of_equipment,
            "safety_measures": self.safety_measures,
            "weekly_utilization": self.weekly_utilization,
            "technical_manpower_ids": [
                str(technical_manpower_id)
                for technical_manpower_id in self.technical_manpower_ids
            ],
        }

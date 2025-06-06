from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class EResources(BaseModel):
    faculty_id: UUID
    name: str
    development_platform: str
    date_of_launch: datetime
    link_to_relevant_document: str
    institute: str

    def to_dict(self):
        return {
            "faculty_id": str(self.faculty_id),
            "name": self.name,
            "development_platform": self.development_platform,
            "date_of_launch": self.date_of_launch.strftime("%Y-%m-%d"),
            "link_to_relevant_document": self.link_to_relevant_document,
            "institute": self.institute,
        }

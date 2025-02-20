from typing import Protocol


class GenericModel(Protocol):
    def to_dict(self) -> dict:
        """Convert the object to a dictionary"""

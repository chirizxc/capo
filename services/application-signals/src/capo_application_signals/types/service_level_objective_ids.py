"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveIds``."""

from typing import TypeAlias

ServiceLevelObjectiveIds: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ServiceLevelObjectiveIds:
    return [item for item in data if item is not None]

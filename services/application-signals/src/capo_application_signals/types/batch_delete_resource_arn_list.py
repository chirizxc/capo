"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteResourceArnList``."""

from typing import TypeAlias

BatchDeleteResourceArnList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> BatchDeleteResourceArnList:
    return [item for item in data if item is not None]

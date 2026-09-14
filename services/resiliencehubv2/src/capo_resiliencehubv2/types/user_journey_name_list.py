"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UserJourneyNameList``."""

from typing import TypeAlias

UserJourneyNameList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: UserJourneyNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> UserJourneyNameList:
    return [item for item in data if item is not None]

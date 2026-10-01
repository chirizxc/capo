"""Generated from Smithy shape ``com.amazonaws.quicksight#GovernedAction``."""

from typing import Literal, TypeAlias, cast

GovernedAction: TypeAlias = Literal["SHARE",]


# --- restJson1 ser/de ---
def serialize_json(value: GovernedAction) -> str:
    return value


def deserialize_json(data: str) -> GovernedAction:
    return cast(GovernedAction, data)

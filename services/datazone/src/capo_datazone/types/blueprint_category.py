"""Generated from Smithy shape ``com.amazonaws.datazone#BlueprintCategory``."""

from typing import Literal, TypeAlias, cast

BlueprintCategory: TypeAlias = Literal["TOOLING",]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintCategory) -> str:
    return value


def deserialize_json(data: str) -> BlueprintCategory:
    return cast(BlueprintCategory, data)

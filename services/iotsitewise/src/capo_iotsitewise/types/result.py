"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Result``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.column_value

Result: TypeAlias = list["capo_iotsitewise.types.column_value.ColumnValue | None"]


# --- restJson1 ser/de ---
def serialize_json(value: Result) -> list:
    return list(value)


def deserialize_json(data: list) -> Result:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.inspector2#ScopeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.scope_value

ScopeValueList: TypeAlias = list["capo_inspector2.types.scope_value.ScopeValue"]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ScopeValueList:
    return [item for item in data if item is not None]

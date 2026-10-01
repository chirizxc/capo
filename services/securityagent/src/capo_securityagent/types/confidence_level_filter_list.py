"""Generated from Smithy shape ``com.amazonaws.securityagent#ConfidenceLevelFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.confidence_level

ConfidenceLevelFilterList: TypeAlias = list[
    "capo_securityagent.types.confidence_level.ConfidenceLevel"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfidenceLevelFilterList) -> list:
    import capo_securityagent.types.confidence_level

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.confidence_level.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfidenceLevelFilterList:
    import capo_securityagent.types.confidence_level

    out: ConfidenceLevelFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.confidence_level.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfOutputUsage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.output_usage

__listOfOutputUsage: TypeAlias = list["capo_medialive.types.output_usage.OutputUsage"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOutputUsage) -> list:
    import capo_medialive.types.output_usage

    out: list = []
    for item in value:
        out.append(capo_medialive.types.output_usage.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOutputUsage:
    import capo_medialive.types.output_usage

    out: __listOfOutputUsage = []
    for item in data:
        if item is None:
            continue
        out.append(capo_medialive.types.output_usage.deserialize_json(item))
    return out

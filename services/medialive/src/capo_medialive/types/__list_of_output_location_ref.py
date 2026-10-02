"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfOutputLocationRef``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.output_location_ref

__listOfOutputLocationRef: TypeAlias = list[
    "capo_medialive.types.output_location_ref.OutputLocationRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOutputLocationRef) -> list:
    import capo_medialive.types.output_location_ref

    out: list = []
    for item in value:
        out.append(capo_medialive.types.output_location_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOutputLocationRef:
    import capo_medialive.types.output_location_ref

    out: __listOfOutputLocationRef = []
    for item in data:
        if item is None:
            continue
        out.append(capo_medialive.types.output_location_ref.deserialize_json(item))
    return out

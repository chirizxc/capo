"""Generated from Smithy shape ``com.amazonaws.appconfig#TreatmentInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.treatment_input

TreatmentInputList: TypeAlias = list[
    "capo_appconfig.types.treatment_input.TreatmentInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: TreatmentInputList) -> list:
    import capo_appconfig.types.treatment_input

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.treatment_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> TreatmentInputList:
    import capo_appconfig.types.treatment_input

    out: TreatmentInputList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appconfig.types.treatment_input.deserialize_json(item))
    return out

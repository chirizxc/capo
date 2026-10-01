"""Generated from Smithy shape ``com.amazonaws.appconfig#TreatmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.treatment

TreatmentList: TypeAlias = list["capo_appconfig.types.treatment.Treatment"]


# --- restJson1 ser/de ---
def serialize_json(value: TreatmentList) -> list:
    import capo_appconfig.types.treatment

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.treatment.serialize_json(item))
    return out


def deserialize_json(data: list) -> TreatmentList:
    import capo_appconfig.types.treatment

    out: TreatmentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appconfig.types.treatment.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.appconfig#TreatmentOverrideMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.entity_id
    import capo_appconfig.types.treatment_key

TreatmentOverrideMap: TypeAlias = dict[
    "capo_appconfig.types.entity_id.EntityId",
    "capo_appconfig.types.treatment_key.TreatmentKey",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TreatmentOverrideMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TreatmentOverrideMap:
    out: TreatmentOverrideMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out

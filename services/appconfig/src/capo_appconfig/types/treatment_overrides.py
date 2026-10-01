"""Generated from Smithy shape ``com.amazonaws.appconfig#TreatmentOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_appconfig.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_appconfig.types.treatment_override_map


class _TreatmentOverrides_Inline(TypedDict, closed=True):
    Inline: "capo_appconfig.types.treatment_override_map.TreatmentOverrideMap"


TreatmentOverrides: TypeAlias = _TreatmentOverrides_Inline


# --- restJson1 ser/de ---
def serialize_json(value: TreatmentOverrides) -> dict:
    if "Inline" in value:
        import capo_appconfig.types.treatment_override_map

        return {
            "Inline": capo_appconfig.types.treatment_override_map.serialize_json(
                value["Inline"]
            )
        }
    else:
        raise SerializationError("TreatmentOverrides: no variant present")


def deserialize_json(data: dict) -> TreatmentOverrides:
    if data.get("Inline") is not None:
        import capo_appconfig.types.treatment_override_map

        return {
            "Inline": capo_appconfig.types.treatment_override_map.deserialize_json(
                data["Inline"]
            )
        }
    else:
        raise DeserializationError("TreatmentOverrides: no recognized variant key")

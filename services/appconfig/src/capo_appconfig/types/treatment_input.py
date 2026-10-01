"""Generated from Smithy shape ``com.amazonaws.appconfig#TreatmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.flag_value
    import capo_appconfig.types.weight


class TreatmentInput(TypedDict, closed=True):
    weight: "capo_appconfig.types.weight.Weight"
    """<p>The traffic allocation weight for this treatment.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the treatment.</p>"""
    flag_value: "capo_appconfig.types.flag_value.FlagValue"
    """<p>The feature flag value to serve to users assigned to this treatment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TreatmentInput) -> dict:
    out: dict = {}
    out["Weight"] = (
        "NaN"
        if value.get("weight", 0) != value.get("weight", 0)
        else "Infinity"
        if value.get("weight", 0) == float("inf")
        else "-Infinity"
        if value.get("weight", 0) == float("-inf")
        else value.get("weight", 0)
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_appconfig.types.flag_value

    out["FlagValue"] = capo_appconfig.types.flag_value.serialize_json(
        value["flag_value"]
    )
    return out


def deserialize_json(data: dict) -> TreatmentInput:
    out: TreatmentInput = {}  # type: ignore[typeddict-item]
    if data.get("Weight") is not None:
        out["weight"] = float(data["Weight"])
    else:
        out["weight"] = 0
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FlagValue") is not None:
        import capo_appconfig.types.flag_value

        out["flag_value"] = capo_appconfig.types.flag_value.deserialize_json(
            data["FlagValue"]
        )
    else:
        raise DeserializationError("TreatmentInput.flag_value required")
    return out

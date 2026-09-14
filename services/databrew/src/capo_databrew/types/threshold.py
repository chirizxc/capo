"""Generated from Smithy shape ``com.amazonaws.databrew#Threshold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.threshold_type
    import capo_databrew.types.threshold_unit
    import capo_databrew.types.threshold_value


class Threshold(TypedDict, closed=True):
    value: "capo_databrew.types.threshold_value.ThresholdValue"
    """<p>The value of a threshold.</p>"""
    type: NotRequired["capo_databrew.types.threshold_type.ThresholdType"]
    """<p>The type of a threshold. Used for comparison of an actual count of rows that satisfy the rule to the threshold value.</p>"""
    unit: NotRequired["capo_databrew.types.threshold_unit.ThresholdUnit"]
    """<p>Unit of threshold value. Can be either a COUNT or PERCENTAGE of the full sample size used for validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Threshold) -> dict:
    out: dict = {}
    out["Value"] = (
        "NaN"
        if value.get("value", 0) != value.get("value", 0)
        else "Infinity"
        if value.get("value", 0) == float("inf")
        else "-Infinity"
        if value.get("value", 0) == float("-inf")
        else value.get("value", 0)
    )
    if "type" in value:
        import capo_databrew.types.threshold_type

        out["Type"] = capo_databrew.types.threshold_type.serialize_json(value["type"])
    if "unit" in value:
        import capo_databrew.types.threshold_unit

        out["Unit"] = capo_databrew.types.threshold_unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> Threshold:
    out: Threshold = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        out["value"] = 0
    if data.get("Type") is not None:
        import capo_databrew.types.threshold_type

        out["type"] = capo_databrew.types.threshold_type.deserialize_json(data["Type"])
    if data.get("Unit") is not None:
        import capo_databrew.types.threshold_unit

        out["unit"] = capo_databrew.types.threshold_unit.deserialize_json(data["Unit"])
    return out

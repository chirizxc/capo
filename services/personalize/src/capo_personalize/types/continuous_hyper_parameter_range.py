"""Generated from Smithy shape ``com.amazonaws.personalize#ContinuousHyperParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.continuous_max_value
    import capo_personalize.types.continuous_min_value
    import capo_personalize.types.parameter_name


class ContinuousHyperParameterRange(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.parameter_name.ParameterName"]
    """<p>The name of the hyperparameter.</p>"""
    min_value: "capo_personalize.types.continuous_min_value.ContinuousMinValue"
    """<p>The minimum allowable value for the hyperparameter.</p>"""
    max_value: "capo_personalize.types.continuous_max_value.ContinuousMaxValue"
    """<p>The maximum allowable value for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousHyperParameterRange) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["minValue"] = (
        "NaN"
        if value.get("min_value", 0) != value.get("min_value", 0)
        else "Infinity"
        if value.get("min_value", 0) == float("inf")
        else "-Infinity"
        if value.get("min_value", 0) == float("-inf")
        else value.get("min_value", 0)
    )
    out["maxValue"] = (
        "NaN"
        if value.get("max_value", 0) != value.get("max_value", 0)
        else "Infinity"
        if value.get("max_value", 0) == float("inf")
        else "-Infinity"
        if value.get("max_value", 0) == float("-inf")
        else value.get("max_value", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContinuousHyperParameterRange:
    out: ContinuousHyperParameterRange = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("minValue") is not None:
        out["min_value"] = float(data["minValue"])
    else:
        out["min_value"] = 0
    if data.get("maxValue") is not None:
        out["max_value"] = float(data["maxValue"])
    else:
        out["max_value"] = 0
    return out

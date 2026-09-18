"""Generated from Smithy shape ``com.amazonaws.personalize#DefaultIntegerHyperParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.integer_max_value
    import capo_personalize.types.integer_min_value
    import capo_personalize.types.parameter_name
    import capo_personalize.types.tunable


class DefaultIntegerHyperParameterRange(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.parameter_name.ParameterName"]
    """<p>The name of the hyperparameter.</p>"""
    min_value: "capo_personalize.types.integer_min_value.IntegerMinValue"
    """<p>The minimum allowable value for the hyperparameter.</p>"""
    max_value: "capo_personalize.types.integer_max_value.IntegerMaxValue"
    """<p>The maximum allowable value for the hyperparameter.</p>"""
    is_tunable: "capo_personalize.types.tunable.Tunable"
    """<p>Indicates whether the hyperparameter is tunable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultIntegerHyperParameterRange) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["minValue"] = value.get("min_value", 0)
    out["maxValue"] = value.get("max_value", 0)
    out["isTunable"] = value.get("is_tunable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultIntegerHyperParameterRange:
    out: DefaultIntegerHyperParameterRange = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("minValue") is not None:
        out["min_value"] = data["minValue"]
    else:
        out["min_value"] = 0
    if data.get("maxValue") is not None:
        out["max_value"] = data["maxValue"]
    else:
        out["max_value"] = 0
    if data.get("isTunable") is not None:
        out["is_tunable"] = data["isTunable"]
    else:
        out["is_tunable"] = False
    return out

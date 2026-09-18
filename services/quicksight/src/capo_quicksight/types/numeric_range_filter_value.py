"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericRangeFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.parameter_name


class NumericRangeFilterValue(TypedDict, closed=True):
    static_value: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The static value of the numeric range filter.</p>"""
    parameter: NotRequired["capo_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter that is used in the numeric range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericRangeFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        out["StaticValue"] = (
            "NaN"
            if value["static_value"] != value["static_value"]
            else "Infinity"
            if value["static_value"] == float("inf")
            else "-Infinity"
            if value["static_value"] == float("-inf")
            else value["static_value"]
        )
    if "parameter" in value:
        out["Parameter"] = value["parameter"]
    return out


def deserialize_json(data: dict) -> NumericRangeFilterValue:
    out: NumericRangeFilterValue = {}  # type: ignore[typeddict-item]
    if data.get("StaticValue") is not None:
        out["static_value"] = float(data["StaticValue"])
    if data.get("Parameter") is not None:
        out["parameter"] = data["Parameter"]
    return out

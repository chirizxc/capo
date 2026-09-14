"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityMetricValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.nullable_double


class DataQualityMetricValues(TypedDict, closed=True):
    actual_value: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The actual value of the data quality metric.</p>"""
    expected_value: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The expected value of the data quality metric according to the analysis of historical data.</p>"""
    lower_limit: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The lower limit of the data quality metric value according to the analysis of historical data.</p>"""
    upper_limit: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The upper limit of the data quality metric value according to the analysis of historical data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityMetricValues) -> dict:
    out: dict = {}
    if "actual_value" in value:
        out["ActualValue"] = (
            "NaN"
            if value["actual_value"] != value["actual_value"]
            else "Infinity"
            if value["actual_value"] == float("inf")
            else "-Infinity"
            if value["actual_value"] == float("-inf")
            else value["actual_value"]
        )
    if "expected_value" in value:
        out["ExpectedValue"] = (
            "NaN"
            if value["expected_value"] != value["expected_value"]
            else "Infinity"
            if value["expected_value"] == float("inf")
            else "-Infinity"
            if value["expected_value"] == float("-inf")
            else value["expected_value"]
        )
    if "lower_limit" in value:
        out["LowerLimit"] = (
            "NaN"
            if value["lower_limit"] != value["lower_limit"]
            else "Infinity"
            if value["lower_limit"] == float("inf")
            else "-Infinity"
            if value["lower_limit"] == float("-inf")
            else value["lower_limit"]
        )
    if "upper_limit" in value:
        out["UpperLimit"] = (
            "NaN"
            if value["upper_limit"] != value["upper_limit"]
            else "Infinity"
            if value["upper_limit"] == float("inf")
            else "-Infinity"
            if value["upper_limit"] == float("-inf")
            else value["upper_limit"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityMetricValues:
    out: DataQualityMetricValues = {}  # type: ignore[typeddict-item]
    if data.get("ActualValue") is not None:
        out["actual_value"] = float(data["ActualValue"])
    if data.get("ExpectedValue") is not None:
        out["expected_value"] = float(data["ExpectedValue"])
    if data.get("LowerLimit") is not None:
        out["lower_limit"] = float(data["LowerLimit"])
    if data.get("UpperLimit") is not None:
        out["upper_limit"] = float(data["UpperLimit"])
    return out

"""Generated from Smithy shape ``com.amazonaws.glue#StatisticModelResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.inclusion_annotation_value
    import capo_glue.types.nullable_double
    import capo_glue.types.timestamp


class StatisticModelResult(TypedDict, closed=True):
    lower_bound: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The lower bound.</p>"""
    upper_bound: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The upper bound.</p>"""
    predicted_value: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The predicted value.</p>"""
    actual_value: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The actual value.</p>"""
    date: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date.</p>"""
    inclusion_annotation: NotRequired[
        "capo_glue.types.inclusion_annotation_value.InclusionAnnotationValue"
    ]
    """<p>The inclusion annotation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticModelResult) -> dict:
    out: dict = {}
    if "lower_bound" in value:
        out["LowerBound"] = (
            "NaN"
            if value["lower_bound"] != value["lower_bound"]
            else "Infinity"
            if value["lower_bound"] == float("inf")
            else "-Infinity"
            if value["lower_bound"] == float("-inf")
            else value["lower_bound"]
        )
    if "upper_bound" in value:
        out["UpperBound"] = (
            "NaN"
            if value["upper_bound"] != value["upper_bound"]
            else "Infinity"
            if value["upper_bound"] == float("inf")
            else "-Infinity"
            if value["upper_bound"] == float("-inf")
            else value["upper_bound"]
        )
    if "predicted_value" in value:
        out["PredictedValue"] = (
            "NaN"
            if value["predicted_value"] != value["predicted_value"]
            else "Infinity"
            if value["predicted_value"] == float("inf")
            else "-Infinity"
            if value["predicted_value"] == float("-inf")
            else value["predicted_value"]
        )
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
    if "date" in value:
        import capo_glue.types.timestamp

        out["Date"] = capo_glue.types.timestamp.serialize_aws_json_1_1(value["date"])
    if "inclusion_annotation" in value:
        import capo_glue.types.inclusion_annotation_value

        out["InclusionAnnotation"] = (
            capo_glue.types.inclusion_annotation_value.serialize_aws_json_1_1(
                value["inclusion_annotation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatisticModelResult:
    out: StatisticModelResult = {}  # type: ignore[typeddict-item]
    if data.get("LowerBound") is not None:
        out["lower_bound"] = float(data["LowerBound"])
    if data.get("UpperBound") is not None:
        out["upper_bound"] = float(data["UpperBound"])
    if data.get("PredictedValue") is not None:
        out["predicted_value"] = float(data["PredictedValue"])
    if data.get("ActualValue") is not None:
        out["actual_value"] = float(data["ActualValue"])
    if data.get("Date") is not None:
        import capo_glue.types.timestamp

        out["date"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(data["Date"])
    if data.get("InclusionAnnotation") is not None:
        import capo_glue.types.inclusion_annotation_value

        out["inclusion_annotation"] = (
            capo_glue.types.inclusion_annotation_value.deserialize_aws_json_1_1(
                data["InclusionAnnotation"]
            )
        )
    return out

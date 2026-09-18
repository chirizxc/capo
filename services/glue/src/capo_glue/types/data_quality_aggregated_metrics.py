"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityAggregatedMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.nullable_double


class DataQualityAggregatedMetrics(TypedDict, closed=True):
    total_rows_processed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of rows that were processed during the data quality evaluation.</p>"""
    total_rows_passed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of rows that passed all applicable data quality rules.</p>"""
    total_rows_failed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of rows that failed one or more data quality rules.</p>"""
    total_rules_processed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of data quality rules that were evaluated.</p>"""
    total_rules_passed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of data quality rules that passed their evaluation criteria.</p>"""
    total_rules_failed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of data quality rules that failed their evaluation criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityAggregatedMetrics) -> dict:
    out: dict = {}
    if "total_rows_processed" in value:
        out["TotalRowsProcessed"] = (
            "NaN"
            if value["total_rows_processed"] != value["total_rows_processed"]
            else "Infinity"
            if value["total_rows_processed"] == float("inf")
            else "-Infinity"
            if value["total_rows_processed"] == float("-inf")
            else value["total_rows_processed"]
        )
    if "total_rows_passed" in value:
        out["TotalRowsPassed"] = (
            "NaN"
            if value["total_rows_passed"] != value["total_rows_passed"]
            else "Infinity"
            if value["total_rows_passed"] == float("inf")
            else "-Infinity"
            if value["total_rows_passed"] == float("-inf")
            else value["total_rows_passed"]
        )
    if "total_rows_failed" in value:
        out["TotalRowsFailed"] = (
            "NaN"
            if value["total_rows_failed"] != value["total_rows_failed"]
            else "Infinity"
            if value["total_rows_failed"] == float("inf")
            else "-Infinity"
            if value["total_rows_failed"] == float("-inf")
            else value["total_rows_failed"]
        )
    if "total_rules_processed" in value:
        out["TotalRulesProcessed"] = (
            "NaN"
            if value["total_rules_processed"] != value["total_rules_processed"]
            else "Infinity"
            if value["total_rules_processed"] == float("inf")
            else "-Infinity"
            if value["total_rules_processed"] == float("-inf")
            else value["total_rules_processed"]
        )
    if "total_rules_passed" in value:
        out["TotalRulesPassed"] = (
            "NaN"
            if value["total_rules_passed"] != value["total_rules_passed"]
            else "Infinity"
            if value["total_rules_passed"] == float("inf")
            else "-Infinity"
            if value["total_rules_passed"] == float("-inf")
            else value["total_rules_passed"]
        )
    if "total_rules_failed" in value:
        out["TotalRulesFailed"] = (
            "NaN"
            if value["total_rules_failed"] != value["total_rules_failed"]
            else "Infinity"
            if value["total_rules_failed"] == float("inf")
            else "-Infinity"
            if value["total_rules_failed"] == float("-inf")
            else value["total_rules_failed"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityAggregatedMetrics:
    out: DataQualityAggregatedMetrics = {}  # type: ignore[typeddict-item]
    if data.get("TotalRowsProcessed") is not None:
        out["total_rows_processed"] = float(data["TotalRowsProcessed"])
    if data.get("TotalRowsPassed") is not None:
        out["total_rows_passed"] = float(data["TotalRowsPassed"])
    if data.get("TotalRowsFailed") is not None:
        out["total_rows_failed"] = float(data["TotalRowsFailed"])
    if data.get("TotalRulesProcessed") is not None:
        out["total_rules_processed"] = float(data["TotalRulesProcessed"])
    if data.get("TotalRulesPassed") is not None:
        out["total_rules_passed"] = float(data["TotalRulesPassed"])
    if data.get("TotalRulesFailed") is not None:
        out["total_rules_failed"] = float(data["TotalRulesFailed"])
    return out

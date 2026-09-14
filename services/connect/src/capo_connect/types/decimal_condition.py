"""Generated from Smithy shape ``com.amazonaws.connect#DecimalCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.decimal_comparison_type
    import capo_connect.types.nullable_double
    import capo_connect.types.string


class DecimalCondition(TypedDict, closed=True):
    field_name: NotRequired["capo_connect.types.string.String"]
    """<p>A name of the decimal property to be searched.</p>"""
    min_value: NotRequired["capo_connect.types.nullable_double.NullableDouble"]
    """<p>A minimum value of the decimal property.</p>"""
    max_value: NotRequired["capo_connect.types.nullable_double.NullableDouble"]
    """<p>A maximum value of the decimal property.</p>"""
    comparison_type: NotRequired[
        "capo_connect.types.decimal_comparison_type.DecimalComparisonType"
    ]
    """<p>The type of comparison to be made when evaluating the decimal condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalCondition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "min_value" in value:
        out["MinValue"] = (
            "NaN"
            if value["min_value"] != value["min_value"]
            else "Infinity"
            if value["min_value"] == float("inf")
            else "-Infinity"
            if value["min_value"] == float("-inf")
            else value["min_value"]
        )
    if "max_value" in value:
        out["MaxValue"] = (
            "NaN"
            if value["max_value"] != value["max_value"]
            else "Infinity"
            if value["max_value"] == float("inf")
            else "-Infinity"
            if value["max_value"] == float("-inf")
            else value["max_value"]
        )
    if "comparison_type" in value:
        import capo_connect.types.decimal_comparison_type

        out["ComparisonType"] = (
            capo_connect.types.decimal_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DecimalCondition:
    out: DecimalCondition = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        out["field_name"] = data["FieldName"]
    if data.get("MinValue") is not None:
        out["min_value"] = float(data["MinValue"])
    if data.get("MaxValue") is not None:
        out["max_value"] = float(data["MaxValue"])
    if data.get("ComparisonType") is not None:
        import capo_connect.types.decimal_comparison_type

        out["comparison_type"] = (
            capo_connect.types.decimal_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out

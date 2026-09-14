"""Generated from Smithy shape ``com.amazonaws.glue#ColumnImportance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_bounded_double
    import capo_glue.types.name_string


class ColumnImportance(TypedDict, closed=True):
    column_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of a column.</p>"""
    importance: NotRequired[
        "capo_glue.types.generic_bounded_double.GenericBoundedDouble"
    ]
    """<p>The column importance score for the column, as a decimal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnImportance) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "importance" in value:
        out["Importance"] = (
            "NaN"
            if value["importance"] != value["importance"]
            else "Infinity"
            if value["importance"] == float("inf")
            else "-Infinity"
            if value["importance"] == float("-inf")
            else value["importance"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnImportance:
    out: ColumnImportance = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    if data.get("Importance") is not None:
        out["importance"] = float(data["Importance"])
    return out

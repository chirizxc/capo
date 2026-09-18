"""Generated from Smithy shape ``com.amazonaws.glue#SchemaColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.column_name_string
    import capo_glue.types.column_type_string


class SchemaColumn(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.column_name_string.ColumnNameString"]
    """<p>The name of the column.</p>"""
    data_type: NotRequired["capo_glue.types.column_type_string.ColumnTypeString"]
    """<p>The type of data in the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaColumn) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaColumn:
    out: SchemaColumn = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    return out

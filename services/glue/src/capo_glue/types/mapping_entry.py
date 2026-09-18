"""Generated from Smithy shape ``com.amazonaws.glue#MappingEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.field_type
    import capo_glue.types.schema_path_string
    import capo_glue.types.table_name


class MappingEntry(TypedDict, closed=True):
    source_table: NotRequired["capo_glue.types.table_name.TableName"]
    """<p>The name of the source table.</p>"""
    source_path: NotRequired["capo_glue.types.schema_path_string.SchemaPathString"]
    """<p>The source path.</p>"""
    source_type: NotRequired["capo_glue.types.field_type.FieldType"]
    """<p>The source type.</p>"""
    target_table: NotRequired["capo_glue.types.table_name.TableName"]
    """<p>The target table.</p>"""
    target_path: NotRequired["capo_glue.types.schema_path_string.SchemaPathString"]
    """<p>The target path.</p>"""
    target_type: NotRequired["capo_glue.types.field_type.FieldType"]
    """<p>The target type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MappingEntry) -> dict:
    out: dict = {}
    if "source_table" in value:
        out["SourceTable"] = value["source_table"]
    if "source_path" in value:
        out["SourcePath"] = value["source_path"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "target_table" in value:
        out["TargetTable"] = value["target_table"]
    if "target_path" in value:
        out["TargetPath"] = value["target_path"]
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MappingEntry:
    out: MappingEntry = {}  # type: ignore[typeddict-item]
    if data.get("SourceTable") is not None:
        out["source_table"] = data["SourceTable"]
    if data.get("SourcePath") is not None:
        out["source_path"] = data["SourcePath"]
    if data.get("SourceType") is not None:
        out["source_type"] = data["SourceType"]
    if data.get("TargetTable") is not None:
        out["target_table"] = data["TargetTable"]
    if data.get("TargetPath") is not None:
        out["target_path"] = data["TargetPath"]
    if data.get("TargetType") is not None:
        out["target_type"] = data["TargetType"]
    return out

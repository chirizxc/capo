"""Generated from Smithy shape ``com.amazonaws.glue#SubObjectStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.nullable_long
    import capo_glue.types.nullable_string
    import capo_glue.types.sub_object_source_type


class SubObjectStatistics(TypedDict, closed=True):
    source_type: NotRequired[
        "capo_glue.types.sub_object_source_type.SubObjectSourceType"
    ]
    """<p>The source type of the sub-object (for example, its table format), which identifies the sub-object.</p>"""
    glue_version_id: NotRequired["capo_glue.types.nullable_string.NullableString"]
    """<p>The Glue version ID of the sub-object that the statistics were captured for.</p>"""
    partition_count: NotRequired["capo_glue.types.nullable_long.NullableLong"]
    """<p>The number of sub-object partitions selected for that refresh. Not present for unpartitioned sub-objects.</p>"""
    file_count: NotRequired["capo_glue.types.nullable_long.NullableLong"]
    """<p>The number of sub-object data files selected for that refresh.</p>"""
    total_file_bytes: NotRequired["capo_glue.types.nullable_long.NullableLong"]
    """<p>The total size, in bytes, of the data files counted by <code>FileCount</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubObjectStatistics) -> dict:
    out: dict = {}
    if "source_type" in value:
        import capo_glue.types.sub_object_source_type

        out["SourceType"] = (
            capo_glue.types.sub_object_source_type.serialize_aws_json_1_1(
                value["source_type"]
            )
        )
    if "glue_version_id" in value:
        out["GlueVersionId"] = value["glue_version_id"]
    if "partition_count" in value:
        out["PartitionCount"] = value["partition_count"]
    if "file_count" in value:
        out["FileCount"] = value["file_count"]
    if "total_file_bytes" in value:
        out["TotalFileBytes"] = value["total_file_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubObjectStatistics:
    out: SubObjectStatistics = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        import capo_glue.types.sub_object_source_type

        out["source_type"] = (
            capo_glue.types.sub_object_source_type.deserialize_aws_json_1_1(
                data["SourceType"]
            )
        )
    if data.get("GlueVersionId") is not None:
        out["glue_version_id"] = data["GlueVersionId"]
    if data.get("PartitionCount") is not None:
        out["partition_count"] = data["PartitionCount"]
    if data.get("FileCount") is not None:
        out["file_count"] = data["FileCount"]
    if data.get("TotalFileBytes") is not None:
        out["total_file_bytes"] = data["TotalFileBytes"]
    return out

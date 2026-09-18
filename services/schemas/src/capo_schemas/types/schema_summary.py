"""Generated from Smithy shape ``com.amazonaws.schemas#SchemaSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__long
    import capo_schemas.types.__string
    import capo_schemas.types.__timestamp_iso8601
    import capo_schemas.types.tags


class SchemaSummary(TypedDict, closed=True):
    last_modified: NotRequired[
        "capo_schemas.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time that schema was modified.</p>"""
    schema_arn: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The ARN of the schema.</p>"""
    schema_name: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The name of the schema.</p>"""
    tags: NotRequired["capo_schemas.types.tags.Tags"]
    """<p>Tags associated with the schema.</p>"""
    version_count: NotRequired["capo_schemas.types.__long.__long"]
    """<p>The number of versions available for the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaSummary) -> dict:
    out: dict = {}
    if "last_modified" in value:
        import capo_schemas.types.__timestamp_iso8601

        out["LastModified"] = capo_schemas.types.__timestamp_iso8601.serialize_json(
            value["last_modified"]
        )
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "tags" in value:
        import capo_schemas.types.tags

        out["tags"] = capo_schemas.types.tags.serialize_json(value["tags"])
    if "version_count" in value:
        out["VersionCount"] = value["version_count"]
    return out


def deserialize_json(data: dict) -> SchemaSummary:
    out: SchemaSummary = {}  # type: ignore[typeddict-item]
    if data.get("LastModified") is not None:
        import capo_schemas.types.__timestamp_iso8601

        out["last_modified"] = capo_schemas.types.__timestamp_iso8601.deserialize_json(
            data["LastModified"]
        )
    if data.get("SchemaArn") is not None:
        out["schema_arn"] = data["SchemaArn"]
    if data.get("SchemaName") is not None:
        out["schema_name"] = data["SchemaName"]
    if data.get("tags") is not None:
        import capo_schemas.types.tags

        out["tags"] = capo_schemas.types.tags.deserialize_json(data["tags"])
    if data.get("VersionCount") is not None:
        out["version_count"] = data["VersionCount"]
    return out

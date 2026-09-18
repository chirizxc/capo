"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#AssetShallow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__string
    import capo_mediapackage_vod.types.tags


class AssetShallow(TypedDict, closed=True):
    arn: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The ARN of the Asset."""
    created_at: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The time the Asset was initially submitted for Ingest."""
    id: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The unique identifier for the Asset."""
    packaging_group_id: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The ID of the PackagingGroup for the Asset."""
    resource_id: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The resource ID to include in SPEKE key requests."""
    source_arn: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """ARN of the source object in S3."""
    source_role_arn: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The IAM role ARN used to access the source S3 bucket."""
    tags: NotRequired["capo_mediapackage_vod.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetShallow) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "id" in value:
        out["id"] = value["id"]
    if "packaging_group_id" in value:
        out["packagingGroupId"] = value["packaging_group_id"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    if "source_role_arn" in value:
        out["sourceRoleArn"] = value["source_role_arn"]
    if "tags" in value:
        import capo_mediapackage_vod.types.tags

        out["tags"] = capo_mediapackage_vod.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetShallow:
    out: AssetShallow = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("packagingGroupId") is not None:
        out["packaging_group_id"] = data["packagingGroupId"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("sourceArn") is not None:
        out["source_arn"] = data["sourceArn"]
    if data.get("sourceRoleArn") is not None:
        out["source_role_arn"] = data["sourceRoleArn"]
    if data.get("tags") is not None:
        import capo_mediapackage_vod.types.tags

        out["tags"] = capo_mediapackage_vod.types.tags.deserialize_json(data["tags"])
    return out

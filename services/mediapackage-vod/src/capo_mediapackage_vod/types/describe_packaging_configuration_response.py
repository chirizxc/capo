"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DescribePackagingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__string
    import capo_mediapackage_vod.types.cmaf_package
    import capo_mediapackage_vod.types.dash_package
    import capo_mediapackage_vod.types.hls_package
    import capo_mediapackage_vod.types.mss_package
    import capo_mediapackage_vod.types.tags


class DescribePackagingConfigurationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The ARN of the PackagingConfiguration."""
    cmaf_package: NotRequired["capo_mediapackage_vod.types.cmaf_package.CmafPackage"]
    created_at: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The time the PackagingConfiguration was created."""
    dash_package: NotRequired["capo_mediapackage_vod.types.dash_package.DashPackage"]
    hls_package: NotRequired["capo_mediapackage_vod.types.hls_package.HlsPackage"]
    id: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The ID of the PackagingConfiguration."""
    mss_package: NotRequired["capo_mediapackage_vod.types.mss_package.MssPackage"]
    packaging_group_id: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The ID of a PackagingGroup."""
    tags: NotRequired["capo_mediapackage_vod.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagingConfigurationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "cmaf_package" in value:
        import capo_mediapackage_vod.types.cmaf_package

        out["cmafPackage"] = capo_mediapackage_vod.types.cmaf_package.serialize_json(
            value["cmaf_package"]
        )
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "dash_package" in value:
        import capo_mediapackage_vod.types.dash_package

        out["dashPackage"] = capo_mediapackage_vod.types.dash_package.serialize_json(
            value["dash_package"]
        )
    if "hls_package" in value:
        import capo_mediapackage_vod.types.hls_package

        out["hlsPackage"] = capo_mediapackage_vod.types.hls_package.serialize_json(
            value["hls_package"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "mss_package" in value:
        import capo_mediapackage_vod.types.mss_package

        out["mssPackage"] = capo_mediapackage_vod.types.mss_package.serialize_json(
            value["mss_package"]
        )
    if "packaging_group_id" in value:
        out["packagingGroupId"] = value["packaging_group_id"]
    if "tags" in value:
        import capo_mediapackage_vod.types.tags

        out["tags"] = capo_mediapackage_vod.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribePackagingConfigurationResponse:
    out: DescribePackagingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("cmafPackage") is not None:
        import capo_mediapackage_vod.types.cmaf_package

        out["cmaf_package"] = capo_mediapackage_vod.types.cmaf_package.deserialize_json(
            data["cmafPackage"]
        )
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("dashPackage") is not None:
        import capo_mediapackage_vod.types.dash_package

        out["dash_package"] = capo_mediapackage_vod.types.dash_package.deserialize_json(
            data["dashPackage"]
        )
    if data.get("hlsPackage") is not None:
        import capo_mediapackage_vod.types.hls_package

        out["hls_package"] = capo_mediapackage_vod.types.hls_package.deserialize_json(
            data["hlsPackage"]
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("mssPackage") is not None:
        import capo_mediapackage_vod.types.mss_package

        out["mss_package"] = capo_mediapackage_vod.types.mss_package.deserialize_json(
            data["mssPackage"]
        )
    if data.get("packagingGroupId") is not None:
        out["packaging_group_id"] = data["packagingGroupId"]
    if data.get("tags") is not None:
        import capo_mediapackage_vod.types.tags

        out["tags"] = capo_mediapackage_vod.types.tags.deserialize_json(data["tags"])
    return out

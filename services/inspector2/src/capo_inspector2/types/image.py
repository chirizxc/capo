"""Generated from Smithy shape ``com.amazonaws.inspector2#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.image_tag_list
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.platform


class Image(TypedDict, closed=True):
    repository_name: NotRequired[
        "capo_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the repository the container image resides in.</p>"""
    registry: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The registry for the container image.</p>"""
    image_tags: NotRequired["capo_inspector2.types.image_tag_list.ImageTagList"]
    """<p>The image tags attached to the container image.</p>"""
    image_digest: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The image digest of the container image.</p>"""
    pushed_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the container image was pushed.</p>"""
    architecture: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The architecture of the container image.</p>"""
    author: NotRequired["str"]
    """<p>The author of the container image.</p>"""
    in_use_count: NotRequired["int"]
    """<p>The number of times the container image is in use.</p>"""
    last_in_use_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The last time the container image was in use.</p>"""
    platform: NotRequired["capo_inspector2.types.platform.Platform"]
    """<p>The platform of the container image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Image) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "registry" in value:
        out["registry"] = value["registry"]
    if "image_tags" in value:
        import capo_inspector2.types.image_tag_list

        out["imageTags"] = capo_inspector2.types.image_tag_list.serialize_json(
            value["image_tags"]
        )
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "pushed_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["pushedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["pushed_at"]
        )
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "author" in value:
        out["author"] = value["author"]
    if "in_use_count" in value:
        out["inUseCount"] = value["in_use_count"]
    if "last_in_use_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastInUseAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["last_in_use_at"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("registry") is not None:
        out["registry"] = data["registry"]
    if data.get("imageTags") is not None:
        import capo_inspector2.types.image_tag_list

        out["image_tags"] = capo_inspector2.types.image_tag_list.deserialize_json(
            data["imageTags"]
        )
    if data.get("imageDigest") is not None:
        out["image_digest"] = data["imageDigest"]
    if data.get("pushedAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["pushed_at"] = capo_inspector2.types.date_time_timestamp.deserialize_json(
            data["pushedAt"]
        )
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("author") is not None:
        out["author"] = data["author"]
    if data.get("inUseCount") is not None:
        out["in_use_count"] = data["inUseCount"]
    if data.get("lastInUseAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["last_in_use_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastInUseAt"]
            )
        )
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    return out

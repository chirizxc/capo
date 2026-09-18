"""Generated from Smithy shape ``com.amazonaws.inspector2#EcrContainerImageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.tag_list


class EcrContainerImageMetadata(TypedDict, closed=True):
    tags: NotRequired["capo_inspector2.types.tag_list.TagList"]
    """<p>Tags associated with the Amazon ECR image metadata.</p>"""
    image_pulled_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date an image was last pulled at.</p>"""
    last_in_use_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.</p>"""
    in_use_count: NotRequired["int"]
    """<p>The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrContainerImageMetadata) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_inspector2.types.tag_list

        out["tags"] = capo_inspector2.types.tag_list.serialize_json(value["tags"])
    if "image_pulled_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["imagePulledAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["image_pulled_at"]
        )
    if "last_in_use_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastInUseAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["last_in_use_at"]
        )
    if "in_use_count" in value:
        out["inUseCount"] = value["in_use_count"]
    return out


def deserialize_json(data: dict) -> EcrContainerImageMetadata:
    out: EcrContainerImageMetadata = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_list

        out["tags"] = capo_inspector2.types.tag_list.deserialize_json(data["tags"])
    if data.get("imagePulledAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["image_pulled_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["imagePulledAt"]
            )
        )
    if data.get("lastInUseAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["last_in_use_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastInUseAt"]
            )
        )
    if data.get("inUseCount") is not None:
        out["in_use_count"] = data["inUseCount"]
    return out

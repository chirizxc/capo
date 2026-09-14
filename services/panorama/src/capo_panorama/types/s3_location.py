"""Generated from Smithy shape ``com.amazonaws.panorama#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.bucket_name
    import capo_panorama.types.object_key
    import capo_panorama.types.region


class S3Location(TypedDict, closed=True):
    region: NotRequired["capo_panorama.types.region.Region"]
    """<p>The bucket's Region.</p>"""
    bucket_name: "capo_panorama.types.bucket_name.BucketName"
    """<p>A bucket name.</p>"""
    object_key: "capo_panorama.types.object_key.ObjectKey"
    """<p>An object key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    out["BucketName"] = value["bucket_name"]
    out["ObjectKey"] = value["object_key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3Location.bucket_name required")
    if data.get("ObjectKey") is not None:
        out["object_key"] = data["ObjectKey"]
    else:
        raise DeserializationError("S3Location.object_key required")
    return out

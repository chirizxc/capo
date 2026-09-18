"""Generated from Smithy shape ``com.amazonaws.iot#S3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.prefix
    import capo_iot.types.s3_bucket


class S3Destination(TypedDict, closed=True):
    bucket: NotRequired["capo_iot.types.s3_bucket.S3Bucket"]
    """<p>The S3 bucket that contains the updated firmware.</p>"""
    prefix: NotRequired["capo_iot.types.prefix.Prefix"]
    """<p>The S3 prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Destination) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out

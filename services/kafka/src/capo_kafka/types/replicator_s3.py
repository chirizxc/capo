"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicatorS3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean
    import capo_kafka.types.__string


class ReplicatorS3(TypedDict, closed=True):
    enabled: NotRequired["capo_kafka.types.__boolean.__boolean"]
    """<p>Whether log delivery to S3 is enabled.</p>"""
    bucket: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The S3 bucket that is the destination for log delivery.</p>"""
    prefix: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The S3 prefix that is the destination for log delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicatorS3) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ReplicatorS3:
    out: ReplicatorS3 = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out

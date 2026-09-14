"""Generated from Smithy shape ``com.amazonaws.kafka#S3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean
    import capo_kafka.types.__string


class S3(TypedDict, closed=True):
    bucket: NotRequired["capo_kafka.types.__string.__string"]
    enabled: NotRequired["capo_kafka.types.__boolean.__boolean"]
    prefix: NotRequired["capo_kafka.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: S3) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3:
    out: S3 = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out

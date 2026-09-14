"""Generated from Smithy shape ``com.amazonaws.cleanrooms#S3Location``."""

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError


class S3Location(TypedDict, closed=True):
    bucket: "str"
    """<p> The bucket name.</p>"""
    key: "str"
    """<p> The object key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("S3Location.bucket required")
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3Location.key required")
    return out

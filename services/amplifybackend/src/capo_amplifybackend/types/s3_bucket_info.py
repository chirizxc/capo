"""Generated from Smithy shape ``com.amazonaws.amplifybackend#S3BucketInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class S3BucketInfo(TypedDict, closed=True):
    creation_date: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The creation date of the S3 bucket.</p>"""
    name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of the S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketInfo) -> dict:
    out: dict = {}
    if "creation_date" in value:
        out["creationDate"] = value["creation_date"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> S3BucketInfo:
    out: S3BucketInfo = {}  # type: ignore[typeddict-item]
    if data.get("creationDate") is not None:
        out["creation_date"] = data["creationDate"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out

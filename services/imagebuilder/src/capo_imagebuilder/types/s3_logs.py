"""Generated from Smithy shape ``com.amazonaws.imagebuilder#S3Logs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.non_empty_string


class S3Logs(TypedDict, closed=True):
    s3_bucket_name: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of an existing Amazon S3 bucket where Image Builder saves build logs. The bucket isn't validated when you create or update the configuration, and Image Builder doesn't create it. The instance profile associated with this infrastructure configuration must have permission to write to the bucket.</p>"""
    s3_key_prefix: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon S3 key prefix under which Image Builder writes build and test logs in the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Logs) -> dict:
    out: dict = {}
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_json(data: dict) -> S3Logs:
    out: S3Logs = {}  # type: ignore[typeddict-item]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    if data.get("s3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    return out

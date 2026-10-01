"""Generated from Smithy shape ``com.amazonaws.kafka#DeadLetterQueueS3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class DeadLetterQueueS3(TypedDict, closed=True):
    bucket_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the dead-letter Amazon S3 bucket.</p>"""
    error_output_prefix: NotRequired["capo_kafka.types.__string.__string"]
    """<p>An optional prefix prepended to every dead-letter Amazon S3 object key.</p>"""
    expected_bucket_owner: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Optional 12-digit AWS account ID expected to own the dead-letter Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeadLetterQueueS3) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["bucketArn"] = value["bucket_arn"]
    if "error_output_prefix" in value:
        out["errorOutputPrefix"] = value["error_output_prefix"]
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    return out


def deserialize_json(data: dict) -> DeadLetterQueueS3:
    out: DeadLetterQueueS3 = {}  # type: ignore[typeddict-item]
    if data.get("bucketArn") is not None:
        out["bucket_arn"] = data["bucketArn"]
    if data.get("errorOutputPrefix") is not None:
        out["error_output_prefix"] = data["errorOutputPrefix"]
    if data.get("expectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    return out

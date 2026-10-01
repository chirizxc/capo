"""Generated from Smithy shape ``com.amazonaws.kafka#S3DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__integer
    import capo_kafka.types.__string
    import capo_kafka.types.dead_letter_queue_s3
    import capo_kafka.types.s3_storage


class S3DestinationConfiguration(TypedDict, closed=True):
    data_freshness_in_seconds: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900. Default: 600.</p>"""
    dead_letter_queue_s3: NotRequired[
        "capo_kafka.types.dead_letter_queue_s3.DeadLetterQueueS3"
    ]
    """<p>The Amazon S3 bucket and prefix where MSK writes records that fail to deliver.</p>"""
    service_execution_role_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that MSK assumes to write to the destination Amazon S3 bucket and the dead-letter bucket.</p>"""
    storage: NotRequired["capo_kafka.types.s3_storage.S3Storage"]
    """<p>The Amazon S3 bucket, prefix, and storage class for delivered records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationConfiguration) -> dict:
    out: dict = {}
    if "data_freshness_in_seconds" in value:
        out["dataFreshnessInSeconds"] = value["data_freshness_in_seconds"]
    if "dead_letter_queue_s3" in value:
        import capo_kafka.types.dead_letter_queue_s3

        out["deadLetterQueueS3"] = capo_kafka.types.dead_letter_queue_s3.serialize_json(
            value["dead_letter_queue_s3"]
        )
    if "service_execution_role_arn" in value:
        out["serviceExecutionRoleArn"] = value["service_execution_role_arn"]
    if "storage" in value:
        import capo_kafka.types.s3_storage

        out["storage"] = capo_kafka.types.s3_storage.serialize_json(value["storage"])
    return out


def deserialize_json(data: dict) -> S3DestinationConfiguration:
    out: S3DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("dataFreshnessInSeconds") is not None:
        out["data_freshness_in_seconds"] = data["dataFreshnessInSeconds"]
    if data.get("deadLetterQueueS3") is not None:
        import capo_kafka.types.dead_letter_queue_s3

        out["dead_letter_queue_s3"] = (
            capo_kafka.types.dead_letter_queue_s3.deserialize_json(
                data["deadLetterQueueS3"]
            )
        )
    if data.get("serviceExecutionRoleArn") is not None:
        out["service_execution_role_arn"] = data["serviceExecutionRoleArn"]
    if data.get("storage") is not None:
        import capo_kafka.types.s3_storage

        out["storage"] = capo_kafka.types.s3_storage.deserialize_json(data["storage"])
    return out

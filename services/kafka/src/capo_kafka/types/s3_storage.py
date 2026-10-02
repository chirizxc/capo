"""Generated from Smithy shape ``com.amazonaws.kafka#S3Storage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.s3_compression_type
    import capo_kafka.types.s3_storage_class


class S3Storage(TypedDict, closed=True):
    bucket_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the destination Amazon S3 bucket.</p>"""
    compression_type: NotRequired[
        "capo_kafka.types.s3_compression_type.S3CompressionType"
    ]
    """<p>The compression codec applied to delivered Amazon S3 objects.</p>"""
    output_prefix: NotRequired["capo_kafka.types.__string.__string"]
    """<p>An optional prefix prepended to every Amazon S3 object key written by the channel.</p>"""
    output_key_template: NotRequired["capo_kafka.types.__string.__string"]
    """<p>An optional template that controls the Amazon S3 object key for each delivered record. Supports the placeholders !{partition-id}, !{sequence-number}, and !{kafka-offset}.</p>"""
    storage_class: NotRequired["capo_kafka.types.s3_storage_class.S3StorageClass"]
    """<p>The Amazon S3 storage class for delivered objects.</p>"""
    expected_bucket_owner: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Optional 12-digit AWS account ID expected to own the Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Storage) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["bucketArn"] = value["bucket_arn"]
    if "compression_type" in value:
        import capo_kafka.types.s3_compression_type

        out["compressionType"] = capo_kafka.types.s3_compression_type.serialize_json(
            value["compression_type"]
        )
    if "output_prefix" in value:
        out["outputPrefix"] = value["output_prefix"]
    if "output_key_template" in value:
        out["outputKeyTemplate"] = value["output_key_template"]
    if "storage_class" in value:
        import capo_kafka.types.s3_storage_class

        out["storageClass"] = capo_kafka.types.s3_storage_class.serialize_json(
            value["storage_class"]
        )
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    return out


def deserialize_json(data: dict) -> S3Storage:
    out: S3Storage = {}  # type: ignore[typeddict-item]
    if data.get("bucketArn") is not None:
        out["bucket_arn"] = data["bucketArn"]
    if data.get("compressionType") is not None:
        import capo_kafka.types.s3_compression_type

        out["compression_type"] = capo_kafka.types.s3_compression_type.deserialize_json(
            data["compressionType"]
        )
    if data.get("outputPrefix") is not None:
        out["output_prefix"] = data["outputPrefix"]
    if data.get("outputKeyTemplate") is not None:
        out["output_key_template"] = data["outputKeyTemplate"]
    if data.get("storageClass") is not None:
        import capo_kafka.types.s3_storage_class

        out["storage_class"] = capo_kafka.types.s3_storage_class.deserialize_json(
            data["storageClass"]
        )
    if data.get("expectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    return out

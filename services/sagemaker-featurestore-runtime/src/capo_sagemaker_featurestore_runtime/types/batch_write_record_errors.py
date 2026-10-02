"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchWriteRecordErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_error

BatchWriteRecordErrors: TypeAlias = list[
    "capo_sagemaker_featurestore_runtime.types.batch_write_record_error.BatchWriteRecordError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteRecordErrors) -> list:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_error

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker_featurestore_runtime.types.batch_write_record_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchWriteRecordErrors:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_error

    out: BatchWriteRecordErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker_featurestore_runtime.types.batch_write_record_error.deserialize_json(
                item
            )
        )
    return out

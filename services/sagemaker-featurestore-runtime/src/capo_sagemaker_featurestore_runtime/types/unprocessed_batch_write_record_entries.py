"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#UnprocessedBatchWriteRecordEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_entry

UnprocessedBatchWriteRecordEntries: TypeAlias = list[
    "capo_sagemaker_featurestore_runtime.types.batch_write_record_entry.BatchWriteRecordEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedBatchWriteRecordEntries) -> list:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_entry

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker_featurestore_runtime.types.batch_write_record_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UnprocessedBatchWriteRecordEntries:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_entry

    out: UnprocessedBatchWriteRecordEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker_featurestore_runtime.types.batch_write_record_entry.deserialize_json(
                item
            )
        )
    return out

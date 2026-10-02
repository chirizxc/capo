"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchWriteRecordResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_errors
    import capo_sagemaker_featurestore_runtime.types.unprocessed_batch_write_record_entries


class BatchWriteRecordResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.batch_write_record_errors.BatchWriteRecordErrors"
    ]
    """<p>A list of errors that occurred when writing records in the batch.</p>"""
    unprocessed_entries: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.unprocessed_batch_write_record_entries.UnprocessedBatchWriteRecordEntries"
    ]
    """<p>A list of entries that were not processed. These entries can be retried.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteRecordResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_sagemaker_featurestore_runtime.types.batch_write_record_errors

        out["Errors"] = (
            capo_sagemaker_featurestore_runtime.types.batch_write_record_errors.serialize_json(
                value["errors"]
            )
        )
    if "unprocessed_entries" in value:
        import capo_sagemaker_featurestore_runtime.types.unprocessed_batch_write_record_entries

        out["UnprocessedEntries"] = (
            capo_sagemaker_featurestore_runtime.types.unprocessed_batch_write_record_entries.serialize_json(
                value["unprocessed_entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchWriteRecordResponse:
    out: BatchWriteRecordResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_sagemaker_featurestore_runtime.types.batch_write_record_errors

        out["errors"] = (
            capo_sagemaker_featurestore_runtime.types.batch_write_record_errors.deserialize_json(
                data["Errors"]
            )
        )
    if data.get("UnprocessedEntries") is not None:
        import capo_sagemaker_featurestore_runtime.types.unprocessed_batch_write_record_entries

        out["unprocessed_entries"] = (
            capo_sagemaker_featurestore_runtime.types.unprocessed_batch_write_record_entries.deserialize_json(
                data["UnprocessedEntries"]
            )
        )
    return out

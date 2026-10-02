"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchWriteRecordError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_write_record_entry
    import capo_sagemaker_featurestore_runtime.types.message
    import capo_sagemaker_featurestore_runtime.types.value_as_string


class BatchWriteRecordError(TypedDict, closed=True):
    entry: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.batch_write_record_entry.BatchWriteRecordEntry"
    ]
    """<p>The entry that failed to be written.</p>"""
    error_code: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The error code for the failed record write.</p>"""
    error_message: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.message.Message"
    ]
    """<p>The error message for the failed record write.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteRecordError) -> dict:
    out: dict = {}
    if "entry" in value:
        import capo_sagemaker_featurestore_runtime.types.batch_write_record_entry

        out["Entry"] = (
            capo_sagemaker_featurestore_runtime.types.batch_write_record_entry.serialize_json(
                value["entry"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchWriteRecordError:
    out: BatchWriteRecordError = {}  # type: ignore[typeddict-item]
    if data.get("Entry") is not None:
        import capo_sagemaker_featurestore_runtime.types.batch_write_record_entry

        out["entry"] = (
            capo_sagemaker_featurestore_runtime.types.batch_write_record_entry.deserialize_json(
                data["Entry"]
            )
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out

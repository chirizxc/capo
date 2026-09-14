"""Generated from Smithy shape ``com.amazonaws.medialive#BatchDeleteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_batch_failed_result_model
    import capo_medialive.types.__list_of_batch_successful_result_model


class BatchDeleteResponse(TypedDict, closed=True):
    failed: NotRequired[
        "capo_medialive.types.__list_of_batch_failed_result_model.__listOfBatchFailedResultModel"
    ]
    """List of failed operations"""
    successful: NotRequired[
        "capo_medialive.types.__list_of_batch_successful_result_model.__listOfBatchSuccessfulResultModel"
    ]
    """List of successful operations"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteResponse) -> dict:
    out: dict = {}
    if "failed" in value:
        import capo_medialive.types.__list_of_batch_failed_result_model

        out["failed"] = (
            capo_medialive.types.__list_of_batch_failed_result_model.serialize_json(
                value["failed"]
            )
        )
    if "successful" in value:
        import capo_medialive.types.__list_of_batch_successful_result_model

        out["successful"] = (
            capo_medialive.types.__list_of_batch_successful_result_model.serialize_json(
                value["successful"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteResponse:
    out: BatchDeleteResponse = {}  # type: ignore[typeddict-item]
    if data.get("failed") is not None:
        import capo_medialive.types.__list_of_batch_failed_result_model

        out["failed"] = (
            capo_medialive.types.__list_of_batch_failed_result_model.deserialize_json(
                data["failed"]
            )
        )
    if data.get("successful") is not None:
        import capo_medialive.types.__list_of_batch_successful_result_model

        out["successful"] = (
            capo_medialive.types.__list_of_batch_successful_result_model.deserialize_json(
                data["successful"]
            )
        )
    return out

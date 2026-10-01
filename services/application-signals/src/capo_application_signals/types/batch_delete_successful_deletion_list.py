"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteSuccessfulDeletionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.batch_delete_successful_deletion

BatchDeleteSuccessfulDeletionList: TypeAlias = list[
    "capo_application_signals.types.batch_delete_successful_deletion.BatchDeleteSuccessfulDeletion"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteSuccessfulDeletionList) -> list:
    import capo_application_signals.types.batch_delete_successful_deletion

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.batch_delete_successful_deletion.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteSuccessfulDeletionList:
    import capo_application_signals.types.batch_delete_successful_deletion

    out: BatchDeleteSuccessfulDeletionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_signals.types.batch_delete_successful_deletion.deserialize_json(
                item
            )
        )
    return out

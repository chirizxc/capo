"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.batch_delete_error

BatchDeleteErrorList: TypeAlias = list[
    "capo_application_signals.types.batch_delete_error.BatchDeleteError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteErrorList) -> list:
    import capo_application_signals.types.batch_delete_error

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.batch_delete_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchDeleteErrorList:
    import capo_application_signals.types.batch_delete_error

    out: BatchDeleteErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_signals.types.batch_delete_error.deserialize_json(item)
        )
    return out

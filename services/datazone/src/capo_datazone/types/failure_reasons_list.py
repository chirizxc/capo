"""Generated from Smithy shape ``com.amazonaws.datazone#FailureReasonsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.failure_reason

FailureReasonsList: TypeAlias = list["capo_datazone.types.failure_reason.FailureReason"]


# --- restJson1 ser/de ---
def serialize_json(value: FailureReasonsList) -> list:
    import capo_datazone.types.failure_reason

    out: list = []
    for item in value:
        out.append(capo_datazone.types.failure_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailureReasonsList:
    import capo_datazone.types.failure_reason

    out: FailureReasonsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.failure_reason.deserialize_json(item))
    return out

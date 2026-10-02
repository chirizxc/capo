"""Generated from Smithy shape ``com.amazonaws.applicationsignals#UnprocessedStatusEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.unprocessed_status_event

UnprocessedStatusEventList: TypeAlias = list[
    "capo_application_signals.types.unprocessed_status_event.UnprocessedStatusEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStatusEventList) -> list:
    import capo_application_signals.types.unprocessed_status_event

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.unprocessed_status_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UnprocessedStatusEventList:
    import capo_application_signals.types.unprocessed_status_event

    out: UnprocessedStatusEventList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_signals.types.unprocessed_status_event.deserialize_json(
                item
            )
        )
    return out

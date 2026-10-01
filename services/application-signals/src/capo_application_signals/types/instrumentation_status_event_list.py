"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationStatusEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.instrumentation_status_event

InstrumentationStatusEventList: TypeAlias = list[
    "capo_application_signals.types.instrumentation_status_event.InstrumentationStatusEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationStatusEventList) -> list:
    import capo_application_signals.types.instrumentation_status_event

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.instrumentation_status_event.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InstrumentationStatusEventList:
    import capo_application_signals.types.instrumentation_status_event

    out: InstrumentationStatusEventList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_signals.types.instrumentation_status_event.deserialize_json(
                item
            )
        )
    return out

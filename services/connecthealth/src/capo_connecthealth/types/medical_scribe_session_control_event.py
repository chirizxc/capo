"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeSessionControlEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_connecthealth.types.medical_scribe_session_control_event_type


class MedicalScribeSessionControlEvent(TypedDict, closed=True):
    type: NotRequired[
        "capo_connecthealth.types.medical_scribe_session_control_event_type.MedicalScribeSessionControlEventType"
    ]
    """<p>The type of session control event</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeSessionControlEvent) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_connecthealth.types.medical_scribe_session_control_event_type

        out["type"] = (
            capo_connecthealth.types.medical_scribe_session_control_event_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeSessionControlEvent:
    out: MedicalScribeSessionControlEvent = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_connecthealth.types.medical_scribe_session_control_event_type

        out["type"] = (
            capo_connecthealth.types.medical_scribe_session_control_event_type.deserialize_json(
                data["type"]
            )
        )
    return out


def serialize_event_json(value: MedicalScribeSessionControlEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "sessionControlEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeSessionControlEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeSessionControlEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out

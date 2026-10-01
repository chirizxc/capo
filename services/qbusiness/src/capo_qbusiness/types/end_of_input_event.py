"""Generated from Smithy shape ``com.amazonaws.qbusiness#EndOfInputEvent``."""

import json

from typing_extensions import TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message


class EndOfInputEvent(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: EndOfInputEvent) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EndOfInputEvent:
    out: EndOfInputEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: EndOfInputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "endOfInputEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> EndOfInputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: EndOfInputEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out

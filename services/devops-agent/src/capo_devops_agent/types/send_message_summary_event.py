"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageSummaryEvent``."""

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent._protocol.eventstream import HeaderValue, Message


class SendMessageSummaryEvent(TypedDict, closed=True):
    content: NotRequired["str"]
    """<p>Summary content</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageSummaryEvent) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageSummaryEvent:
    out: SendMessageSummaryEvent = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("sequenceNumber") is not None:
        out["sequence_number"] = data["sequenceNumber"]
    return out


def serialize_event_json(value: SendMessageSummaryEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "summary"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageSummaryEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageSummaryEvent = {}  # type: ignore[typeddict-item]
    return out

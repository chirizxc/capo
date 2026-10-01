"""Generated from Smithy shape ``com.amazonaws.kafka#ChannelStateInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class ChannelStateInfo(TypedDict, closed=True):
    code: NotRequired["capo_kafka.types.__string.__string"]
    """<p>A short, machine-readable code identifying the failure cause.</p>"""
    message: NotRequired["capo_kafka.types.__string.__string"]
    """<p>A human-readable message describing the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelStateInfo) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ChannelStateInfo:
    out: ChannelStateInfo = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out

"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicatorFirehose``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean
    import capo_kafka.types.__string


class ReplicatorFirehose(TypedDict, closed=True):
    enabled: NotRequired["capo_kafka.types.__boolean.__boolean"]
    """<p>Whether log delivery to Firehose is enabled.</p>"""
    delivery_stream: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Firehose delivery stream that is the destination for log delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicatorFirehose) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "delivery_stream" in value:
        out["deliveryStream"] = value["delivery_stream"]
    return out


def deserialize_json(data: dict) -> ReplicatorFirehose:
    out: ReplicatorFirehose = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("deliveryStream") is not None:
        out["delivery_stream"] = data["deliveryStream"]
    return out

"""Generated from Smithy shape ``com.amazonaws.kafka#PartitionSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class PartitionSource(TypedDict, closed=True):
    source_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Source name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PartitionSource) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    return out


def deserialize_json(data: dict) -> PartitionSource:
    out: PartitionSource = {}  # type: ignore[typeddict-item]
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    return out

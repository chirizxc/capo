"""Generated from Smithy shape ``com.amazonaws.kafka#S3DestinationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__integer


class S3DestinationUpdate(TypedDict, closed=True):
    data_freshness_in_seconds: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationUpdate) -> dict:
    out: dict = {}
    if "data_freshness_in_seconds" in value:
        out["dataFreshnessInSeconds"] = value["data_freshness_in_seconds"]
    return out


def deserialize_json(data: dict) -> S3DestinationUpdate:
    out: S3DestinationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("dataFreshnessInSeconds") is not None:
        out["data_freshness_in_seconds"] = data["dataFreshnessInSeconds"]
    return out

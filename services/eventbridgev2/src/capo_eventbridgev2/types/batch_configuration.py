"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#BatchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.nullable_integer


class BatchConfiguration(TypedDict, closed=True):
    max_batch_size: NotRequired[
        "capo_eventbridgev2.types.nullable_integer.NullableInteger"
    ]
    """The maximum number of events to include in a single batch delivered to the target. The service delivers up to this many events per batch; fewer may be delivered when the batch window elapses or the target's per-batch limit is smaller. This is a maximum, not a guaranteed count. Valid range is 1-500 (default: 10, or the target API's per-batch maximum). The resolved value applied by the service is returned on read."""
    max_batch_window_in_seconds: NotRequired[
        "capo_eventbridgev2.types.nullable_integer.NullableInteger"
    ]
    """The maximum time in seconds to wait for a batch to fill before delivering it to the target. This is a maximum; a batch may be delivered sooner if it reaches MaxBatchSize or another delivery condition is met. Valid range is 0-300 (default: 0, meaning no wait). The resolved value applied by the service is always returned on read."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchConfiguration) -> dict:
    out: dict = {}
    if "max_batch_size" in value:
        out["MaxBatchSize"] = value["max_batch_size"]
    if "max_batch_window_in_seconds" in value:
        out["MaxBatchWindowInSeconds"] = value["max_batch_window_in_seconds"]
    return out


def deserialize_cbor(data: dict) -> BatchConfiguration:
    out: BatchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MaxBatchSize") is not None:
        out["max_batch_size"] = data["MaxBatchSize"]
    if data.get("MaxBatchWindowInSeconds") is not None:
        out["max_batch_window_in_seconds"] = data["MaxBatchWindowInSeconds"]
    return out

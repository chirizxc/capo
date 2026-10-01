"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#PartialResults``."""

from typing_extensions import NotRequired, TypedDict


class PartialResults(TypedDict, closed=True):
    partial_results_detected: NotRequired["bool"]
    """True when the query returned partial results (some data could not be read)."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartialResults) -> dict:
    out: dict = {}
    if "partial_results_detected" in value:
        out["partialResultsDetected"] = value["partial_results_detected"]
    return out


def deserialize_cbor(data: dict) -> PartialResults:
    out: PartialResults = {}  # type: ignore[typeddict-item]
    if data.get("partialResultsDetected") is not None:
        out["partial_results_detected"] = data["partialResultsDetected"]
    return out

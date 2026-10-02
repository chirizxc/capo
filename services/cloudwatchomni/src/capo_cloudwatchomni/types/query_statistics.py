"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#QueryStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.partial_results


class QueryStatistics(TypedDict, closed=True):
    bytes_scanned: NotRequired["float"]
    """The number of bytes scanned by the query."""
    percent_complete: NotRequired["int"]
    """The percentage of the query that has completed."""
    records_scanned: NotRequired["int"]
    """The total number of records scanned."""
    records_matched: NotRequired["int"]
    """The number of records that matched the query criteria."""
    partial_results: NotRequired[
        "capo_cloudwatchomni.types.partial_results.PartialResults"
    ]
    """Information about whether the query returned partial results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: QueryStatistics) -> dict:
    out: dict = {}
    if "bytes_scanned" in value:
        out["bytesScanned"] = value["bytes_scanned"]
    if "percent_complete" in value:
        out["percentComplete"] = value["percent_complete"]
    if "records_scanned" in value:
        out["recordsScanned"] = value["records_scanned"]
    if "records_matched" in value:
        out["recordsMatched"] = value["records_matched"]
    if "partial_results" in value:
        import capo_cloudwatchomni.types.partial_results

        out["partialResults"] = (
            capo_cloudwatchomni.types.partial_results.serialize_cbor(
                value["partial_results"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> QueryStatistics:
    out: QueryStatistics = {}  # type: ignore[typeddict-item]
    if data.get("bytesScanned") is not None:
        out["bytes_scanned"] = float(data["bytesScanned"])
    if data.get("percentComplete") is not None:
        out["percent_complete"] = data["percentComplete"]
    if data.get("recordsScanned") is not None:
        out["records_scanned"] = data["recordsScanned"]
    if data.get("recordsMatched") is not None:
        out["records_matched"] = data["recordsMatched"]
    if data.get("partialResults") is not None:
        import capo_cloudwatchomni.types.partial_results

        out["partial_results"] = (
            capo_cloudwatchomni.types.partial_results.deserialize_cbor(
                data["partialResults"]
            )
        )
    return out

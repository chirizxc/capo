"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.consumed_capacity_units


class VectorCapacity(TypedDict, closed=True):
    vector_search_request_bytes: NotRequired[
        "capo_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The number of vector search request bytes consumed by a <code>SearchVectors</code> operation.</p>"""
    vector_write_request_bytes: NotRequired[
        "capo_dynamodb.types.consumed_capacity_units.ConsumedCapacityUnits"
    ]
    """<p>The number of vector write request bytes consumed when writing to a vector index. Reported for write operations that modify attributes indexed by a vector index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorCapacity) -> dict:
    out: dict = {}
    if "vector_search_request_bytes" in value:
        out["VectorSearchRequestBytes"] = (
            "NaN"
            if value["vector_search_request_bytes"]
            != value["vector_search_request_bytes"]
            else "Infinity"
            if value["vector_search_request_bytes"] == float("inf")
            else "-Infinity"
            if value["vector_search_request_bytes"] == float("-inf")
            else value["vector_search_request_bytes"]
        )
    if "vector_write_request_bytes" in value:
        out["VectorWriteRequestBytes"] = (
            "NaN"
            if value["vector_write_request_bytes"]
            != value["vector_write_request_bytes"]
            else "Infinity"
            if value["vector_write_request_bytes"] == float("inf")
            else "-Infinity"
            if value["vector_write_request_bytes"] == float("-inf")
            else value["vector_write_request_bytes"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorCapacity:
    out: VectorCapacity = {}  # type: ignore[typeddict-item]
    if data.get("VectorSearchRequestBytes") is not None:
        out["vector_search_request_bytes"] = float(data["VectorSearchRequestBytes"])
    if data.get("VectorWriteRequestBytes") is not None:
        out["vector_write_request_bytes"] = float(data["VectorWriteRequestBytes"])
    return out

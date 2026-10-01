"""Generated from Smithy shape ``com.amazonaws.dynamodb#SearchVectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.search_result_list
    import capo_dynamodb.types.vector_capacity


class SearchVectorsOutput(TypedDict, closed=True):
    consumed_capacity: NotRequired["capo_dynamodb.types.vector_capacity.VectorCapacity"]
    """<p>The capacity units consumed by the <code>SearchVectors</code> operation. Contains <code>VectorSearchRequestBytes</code>, which represents the vector search capacity consumed.</p>"""
    search_results: NotRequired[
        "capo_dynamodb.types.search_result_list.SearchResultList"
    ]
    """<p>A list of items returned by the vector similarity search, sorted by similarity with the most similar item first. Each item contains the projected attributes and a similarity score.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchVectorsOutput) -> dict:
    out: dict = {}
    if "consumed_capacity" in value:
        import capo_dynamodb.types.vector_capacity

        out["ConsumedCapacity"] = (
            capo_dynamodb.types.vector_capacity.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    if "search_results" in value:
        import capo_dynamodb.types.search_result_list

        out["SearchResults"] = (
            capo_dynamodb.types.search_result_list.serialize_aws_json_1_0(
                value["search_results"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchVectorsOutput:
    out: SearchVectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ConsumedCapacity") is not None:
        import capo_dynamodb.types.vector_capacity

        out["consumed_capacity"] = (
            capo_dynamodb.types.vector_capacity.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    if data.get("SearchResults") is not None:
        import capo_dynamodb.types.search_result_list

        out["search_results"] = (
            capo_dynamodb.types.search_result_list.deserialize_aws_json_1_0(
                data["SearchResults"]
            )
        )
    return out

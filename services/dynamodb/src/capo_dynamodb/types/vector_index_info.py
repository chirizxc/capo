"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndexInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.positive_long_object
    import capo_dynamodb.types.projection
    import capo_dynamodb.types.search_schema
    import capo_dynamodb.types.vector_attribute_definition
    import capo_dynamodb.types.vector_distance_function


class VectorIndexInfo(TypedDict, closed=True):
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The name of the vector index.</p>"""
    vector_attribute: NotRequired[
        "capo_dynamodb.types.vector_attribute_definition.VectorAttributeDefinition"
    ]
    """<p>The vector attribute configuration for the index.</p>"""
    search_schema: NotRequired["capo_dynamodb.types.search_schema.SearchSchema"]
    """<p>The search schema that defines partition key and inline filter attributes for the vector index.</p>"""
    projection: NotRequired["capo_dynamodb.types.projection.Projection"]
    """<p>Specifies attributes that are copied (projected) from the table into the vector index.</p>"""
    dimensions: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The number of dimensions in each vector.</p>"""
    distance_function: NotRequired[
        "capo_dynamodb.types.vector_distance_function.VectorDistanceFunction"
    ]
    """<p>The distance function used to calculate similarity between vectors.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorIndexInfo) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "vector_attribute" in value:
        import capo_dynamodb.types.vector_attribute_definition

        out["VectorAttribute"] = (
            capo_dynamodb.types.vector_attribute_definition.serialize_aws_json_1_0(
                value["vector_attribute"]
            )
        )
    if "search_schema" in value:
        import capo_dynamodb.types.search_schema

        out["SearchSchema"] = capo_dynamodb.types.search_schema.serialize_aws_json_1_0(
            value["search_schema"]
        )
    if "projection" in value:
        import capo_dynamodb.types.projection

        out["Projection"] = capo_dynamodb.types.projection.serialize_aws_json_1_0(
            value["projection"]
        )
    if "dimensions" in value:
        out["Dimensions"] = value["dimensions"]
    if "distance_function" in value:
        import capo_dynamodb.types.vector_distance_function

        out["DistanceFunction"] = (
            capo_dynamodb.types.vector_distance_function.serialize_aws_json_1_0(
                value["distance_function"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorIndexInfo:
    out: VectorIndexInfo = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    if data.get("VectorAttribute") is not None:
        import capo_dynamodb.types.vector_attribute_definition

        out["vector_attribute"] = (
            capo_dynamodb.types.vector_attribute_definition.deserialize_aws_json_1_0(
                data["VectorAttribute"]
            )
        )
    if data.get("SearchSchema") is not None:
        import capo_dynamodb.types.search_schema

        out["search_schema"] = (
            capo_dynamodb.types.search_schema.deserialize_aws_json_1_0(
                data["SearchSchema"]
            )
        )
    if data.get("Projection") is not None:
        import capo_dynamodb.types.projection

        out["projection"] = capo_dynamodb.types.projection.deserialize_aws_json_1_0(
            data["Projection"]
        )
    if data.get("Dimensions") is not None:
        out["dimensions"] = data["Dimensions"]
    if data.get("DistanceFunction") is not None:
        import capo_dynamodb.types.vector_distance_function

        out["distance_function"] = (
            capo_dynamodb.types.vector_distance_function.deserialize_aws_json_1_0(
                data["DistanceFunction"]
            )
        )
    return out

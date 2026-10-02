"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndexDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backfilling
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.index_status
    import capo_dynamodb.types.long_object
    import capo_dynamodb.types.positive_long_object
    import capo_dynamodb.types.projection
    import capo_dynamodb.types.search_schema
    import capo_dynamodb.types.string
    import capo_dynamodb.types.vector_attribute_definition
    import capo_dynamodb.types.vector_distance_function


class VectorIndexDescription(TypedDict, closed=True):
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The name of the vector index.</p>"""
    search_schema: NotRequired["capo_dynamodb.types.search_schema.SearchSchema"]
    """<p>The search schema that defines partition key and inline filter attributes for the vector index.</p>"""
    projection: NotRequired["capo_dynamodb.types.projection.Projection"]
    """<p>Specifies attributes that are copied (projected) from the table into the vector index.</p>"""
    vector_attribute: NotRequired[
        "capo_dynamodb.types.vector_attribute_definition.VectorAttributeDefinition"
    ]
    """<p>The vector attribute configuration for the index.</p>"""
    dimensions: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The number of dimensions in each vector.</p>"""
    distance_function: NotRequired[
        "capo_dynamodb.types.vector_distance_function.VectorDistanceFunction"
    ]
    """<p>The distance function used to calculate similarity between vectors.</p>"""
    index_status: NotRequired["capo_dynamodb.types.index_status.IndexStatus"]
    """<p>The current state of the vector index:</p> <ul> <li> <p> <code>CREATING</code> - The index is being created.</p> </li> <li> <p> <code>ACTIVE</code> - The index is ready for use.</p> </li> <li> <p> <code>DELETING</code> - The index is being deleted.</p> </li> </ul>"""
    backfilling: NotRequired["capo_dynamodb.types.backfilling.Backfilling"]
    """<p>Specifies whether the index is currently backfilling. During backfill, <code>SearchVectors</code> operations might return incomplete results.</p>"""
    index_size_bytes: NotRequired["capo_dynamodb.types.long_object.LongObject"]
    """<p>The total size of the vector index, in bytes. Amazon DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    item_count: NotRequired["capo_dynamodb.types.long_object.LongObject"]
    """<p>The number of items indexed in the vector index. Amazon DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    index_arn: NotRequired["capo_dynamodb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the vector index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorIndexDescription) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
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
    if "vector_attribute" in value:
        import capo_dynamodb.types.vector_attribute_definition

        out["VectorAttribute"] = (
            capo_dynamodb.types.vector_attribute_definition.serialize_aws_json_1_0(
                value["vector_attribute"]
            )
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
    if "index_status" in value:
        import capo_dynamodb.types.index_status

        out["IndexStatus"] = capo_dynamodb.types.index_status.serialize_aws_json_1_0(
            value["index_status"]
        )
    if "backfilling" in value:
        out["Backfilling"] = value["backfilling"]
    if "index_size_bytes" in value:
        out["IndexSizeBytes"] = value["index_size_bytes"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "index_arn" in value:
        out["IndexArn"] = value["index_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorIndexDescription:
    out: VectorIndexDescription = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
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
    if data.get("VectorAttribute") is not None:
        import capo_dynamodb.types.vector_attribute_definition

        out["vector_attribute"] = (
            capo_dynamodb.types.vector_attribute_definition.deserialize_aws_json_1_0(
                data["VectorAttribute"]
            )
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
    if data.get("IndexStatus") is not None:
        import capo_dynamodb.types.index_status

        out["index_status"] = capo_dynamodb.types.index_status.deserialize_aws_json_1_0(
            data["IndexStatus"]
        )
    if data.get("Backfilling") is not None:
        out["backfilling"] = data["Backfilling"]
    if data.get("IndexSizeBytes") is not None:
        out["index_size_bytes"] = data["IndexSizeBytes"]
    if data.get("ItemCount") is not None:
        out["item_count"] = data["ItemCount"]
    if data.get("IndexArn") is not None:
        out["index_arn"] = data["IndexArn"]
    return out

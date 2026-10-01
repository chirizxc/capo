"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndexesCapacityMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.vector_capacity

VectorIndexesCapacityMap: TypeAlias = dict[
    "capo_dynamodb.types.index_name.IndexName",
    "capo_dynamodb.types.vector_capacity.VectorCapacity",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: VectorIndexesCapacityMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.vector_capacity

        out[key] = capo_dynamodb.types.vector_capacity.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorIndexesCapacityMap:
    out: VectorIndexesCapacityMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_dynamodb.types.vector_capacity

        out[key] = capo_dynamodb.types.vector_capacity.deserialize_aws_json_1_0(value)
    return out

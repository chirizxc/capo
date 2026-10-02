"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.vector_index_info

VectorIndexes: TypeAlias = list["capo_dynamodb.types.vector_index_info.VectorIndexInfo"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorIndexes) -> list:
    import capo_dynamodb.types.vector_index_info

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.vector_index_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VectorIndexes:
    import capo_dynamodb.types.vector_index_info

    out: VectorIndexes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dynamodb.types.vector_index_info.deserialize_aws_json_1_0(item))
    return out

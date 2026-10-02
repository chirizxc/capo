"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndexUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.vector_index_update

VectorIndexUpdateList: TypeAlias = list[
    "capo_dynamodb.types.vector_index_update.VectorIndexUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorIndexUpdateList) -> list:
    import capo_dynamodb.types.vector_index_update

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.vector_index_update.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VectorIndexUpdateList:
    import capo_dynamodb.types.vector_index_update

    out: VectorIndexUpdateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.vector_index_update.deserialize_aws_json_1_0(item)
        )
    return out

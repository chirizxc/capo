"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndexDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.vector_index_description

VectorIndexDescriptionList: TypeAlias = list[
    "capo_dynamodb.types.vector_index_description.VectorIndexDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorIndexDescriptionList) -> list:
    import capo_dynamodb.types.vector_index_description

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.vector_index_description.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VectorIndexDescriptionList:
    import capo_dynamodb.types.vector_index_description

    out: VectorIndexDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.vector_index_description.deserialize_aws_json_1_0(item)
        )
    return out

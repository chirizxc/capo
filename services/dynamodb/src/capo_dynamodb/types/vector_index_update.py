"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndexUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.create_vector_index_action
    import capo_dynamodb.types.delete_vector_index_action


class VectorIndexUpdate(TypedDict, closed=True):
    create: NotRequired[
        "capo_dynamodb.types.create_vector_index_action.CreateVectorIndexAction"
    ]
    """<p>The configuration for creating a new vector index on the table.</p>"""
    delete: NotRequired[
        "capo_dynamodb.types.delete_vector_index_action.DeleteVectorIndexAction"
    ]
    """<p>The configuration for deleting an existing vector index from the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorIndexUpdate) -> dict:
    out: dict = {}
    if "create" in value:
        import capo_dynamodb.types.create_vector_index_action

        out["Create"] = (
            capo_dynamodb.types.create_vector_index_action.serialize_aws_json_1_0(
                value["create"]
            )
        )
    if "delete" in value:
        import capo_dynamodb.types.delete_vector_index_action

        out["Delete"] = (
            capo_dynamodb.types.delete_vector_index_action.serialize_aws_json_1_0(
                value["delete"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorIndexUpdate:
    out: VectorIndexUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Create") is not None:
        import capo_dynamodb.types.create_vector_index_action

        out["create"] = (
            capo_dynamodb.types.create_vector_index_action.deserialize_aws_json_1_0(
                data["Create"]
            )
        )
    if data.get("Delete") is not None:
        import capo_dynamodb.types.delete_vector_index_action

        out["delete"] = (
            capo_dynamodb.types.delete_vector_index_action.deserialize_aws_json_1_0(
                data["Delete"]
            )
        )
    return out

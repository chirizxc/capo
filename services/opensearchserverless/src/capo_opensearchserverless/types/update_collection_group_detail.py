"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionGroupDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_group_capacity_limits
    import capo_opensearchserverless.types.collection_group_id
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.serverless_generation


class UpdateCollectionGroupDetail(TypedDict, closed=True):
    id: NotRequired[
        "capo_opensearchserverless.types.collection_group_id.CollectionGroupId"
    ]
    """<p>The unique identifier of the collection group.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the collection group.</p>"""
    name: NotRequired[
        "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>The name of the collection group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the collection group.</p>"""
    capacity_limits: NotRequired[
        "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    """<p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>"""
    created_date: NotRequired["int"]
    """<p>The Epoch time when the collection group was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The date and time when the collection group was last modified.</p>"""
    generation: NotRequired[
        "capo_opensearchserverless.types.serverless_generation.ServerlessGeneration"
    ]
    """<p>The generation of Amazon OpenSearch Serverless for the collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionGroupDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "capacity_limits" in value:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    if "generation" in value:
        out["generation"] = value["generation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionGroupDetail:
    out: UpdateCollectionGroupDetail = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("capacityLimits") is not None:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if data.get("createdDate") is not None:
        out["created_date"] = data["createdDate"]
    if data.get("lastModifiedDate") is not None:
        out["last_modified_date"] = data["lastModifiedDate"]
    if data.get("generation") is not None:
        out["generation"] = data["generation"]
    return out

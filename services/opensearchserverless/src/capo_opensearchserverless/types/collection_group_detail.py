"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_group_capacity_limits
    import capo_opensearchserverless.types.collection_group_id
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.current_capacity
    import capo_opensearchserverless.types.serverless_generation
    import capo_opensearchserverless.types.standby_replicas
    import capo_opensearchserverless.types.tags


class CollectionGroupDetail(TypedDict, closed=True):
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
    standby_replicas: NotRequired[
        "capo_opensearchserverless.types.standby_replicas.StandbyReplicas"
    ]
    """<p>Indicates whether standby replicas are used for the collection group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the collection group.</p>"""
    tags: NotRequired["capo_opensearchserverless.types.tags.Tags"]
    """<p>A map of key-value pairs associated with the collection group.</p>"""
    created_date: NotRequired["int"]
    """<p>The Epoch time when the collection group was created.</p>"""
    capacity_limits: NotRequired[
        "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    """<p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>"""
    current_capacity: NotRequired[
        "capo_opensearchserverless.types.current_capacity.CurrentCapacity"
    ]
    """<p>Current search and indexing capacity for the collection group.</p>"""
    number_of_collections: NotRequired["int"]
    """<p>The number of collections associated with the collection group.</p>"""
    generation: NotRequired[
        "capo_opensearchserverless.types.serverless_generation.ServerlessGeneration"
    ]
    """<p>The generation of Amazon OpenSearch Serverless for the collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "standby_replicas" in value:
        out["standbyReplicas"] = value["standby_replicas"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "capacity_limits" in value:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    if "current_capacity" in value:
        import capo_opensearchserverless.types.current_capacity

        out["currentCapacity"] = (
            capo_opensearchserverless.types.current_capacity.serialize_aws_json_1_0(
                value["current_capacity"]
            )
        )
    if "number_of_collections" in value:
        out["numberOfCollections"] = value["number_of_collections"]
    if "generation" in value:
        out["generation"] = value["generation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionGroupDetail:
    out: CollectionGroupDetail = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("standbyReplicas") is not None:
        out["standby_replicas"] = data["standbyReplicas"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("createdDate") is not None:
        out["created_date"] = data["createdDate"]
    if data.get("capacityLimits") is not None:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if data.get("currentCapacity") is not None:
        import capo_opensearchserverless.types.current_capacity

        out["current_capacity"] = (
            capo_opensearchserverless.types.current_capacity.deserialize_aws_json_1_0(
                data["currentCapacity"]
            )
        )
    if data.get("numberOfCollections") is not None:
        out["number_of_collections"] = data["numberOfCollections"]
    if data.get("generation") is not None:
        out["generation"] = data["generation"]
    return out

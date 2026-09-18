"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.collection_name
    import capo_opensearchserverless.types.collection_status


class CollectionFilters(TypedDict, closed=True):
    name: NotRequired["capo_opensearchserverless.types.collection_name.CollectionName"]
    """<p>The name of the collection.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.collection_status.CollectionStatus"
    ]
    """<p>The current status of the collection.</p>"""
    collection_group_name: NotRequired[
        "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>The name of the collection group to filter by.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionFilters) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "collection_group_name" in value:
        out["collectionGroupName"] = value["collection_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionFilters:
    out: CollectionFilters = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("collectionGroupName") is not None:
        out["collection_group_name"] = data["collectionGroupName"]
    return out

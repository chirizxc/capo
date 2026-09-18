"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupCapacityLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_group_max_indexing_capacity_value
    import capo_opensearchserverless.types.collection_group_max_search_capacity_value
    import capo_opensearchserverless.types.collection_group_min_indexing_capacity_value
    import capo_opensearchserverless.types.collection_group_min_search_capacity_value


class CollectionGroupCapacityLimits(TypedDict, closed=True):
    max_indexing_capacity_in_ocu: NotRequired[
        "capo_opensearchserverless.types.collection_group_max_indexing_capacity_value.CollectionGroupMaxIndexingCapacityValue"
    ]
    """<p>The maximum indexing capacity for collections in the group.</p>"""
    max_search_capacity_in_ocu: NotRequired[
        "capo_opensearchserverless.types.collection_group_max_search_capacity_value.CollectionGroupMaxSearchCapacityValue"
    ]
    """<p>The maximum search capacity for collections in the group.</p>"""
    min_indexing_capacity_in_ocu: NotRequired[
        "capo_opensearchserverless.types.collection_group_min_indexing_capacity_value.CollectionGroupMinIndexingCapacityValue"
    ]
    """<p>The minimum indexing capacity for collections in the group.</p>"""
    min_search_capacity_in_ocu: NotRequired[
        "capo_opensearchserverless.types.collection_group_min_search_capacity_value.CollectionGroupMinSearchCapacityValue"
    ]
    """<p>The minimum search capacity for collections in the group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupCapacityLimits) -> dict:
    out: dict = {}
    if "max_indexing_capacity_in_ocu" in value:
        out["maxIndexingCapacityInOCU"] = (
            "NaN"
            if value["max_indexing_capacity_in_ocu"]
            != value["max_indexing_capacity_in_ocu"]
            else "Infinity"
            if value["max_indexing_capacity_in_ocu"] == float("inf")
            else "-Infinity"
            if value["max_indexing_capacity_in_ocu"] == float("-inf")
            else value["max_indexing_capacity_in_ocu"]
        )
    if "max_search_capacity_in_ocu" in value:
        out["maxSearchCapacityInOCU"] = (
            "NaN"
            if value["max_search_capacity_in_ocu"]
            != value["max_search_capacity_in_ocu"]
            else "Infinity"
            if value["max_search_capacity_in_ocu"] == float("inf")
            else "-Infinity"
            if value["max_search_capacity_in_ocu"] == float("-inf")
            else value["max_search_capacity_in_ocu"]
        )
    if "min_indexing_capacity_in_ocu" in value:
        out["minIndexingCapacityInOCU"] = (
            "NaN"
            if value["min_indexing_capacity_in_ocu"]
            != value["min_indexing_capacity_in_ocu"]
            else "Infinity"
            if value["min_indexing_capacity_in_ocu"] == float("inf")
            else "-Infinity"
            if value["min_indexing_capacity_in_ocu"] == float("-inf")
            else value["min_indexing_capacity_in_ocu"]
        )
    if "min_search_capacity_in_ocu" in value:
        out["minSearchCapacityInOCU"] = (
            "NaN"
            if value["min_search_capacity_in_ocu"]
            != value["min_search_capacity_in_ocu"]
            else "Infinity"
            if value["min_search_capacity_in_ocu"] == float("inf")
            else "-Infinity"
            if value["min_search_capacity_in_ocu"] == float("-inf")
            else value["min_search_capacity_in_ocu"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionGroupCapacityLimits:
    out: CollectionGroupCapacityLimits = {}  # type: ignore[typeddict-item]
    if data.get("maxIndexingCapacityInOCU") is not None:
        out["max_indexing_capacity_in_ocu"] = float(data["maxIndexingCapacityInOCU"])
    if data.get("maxSearchCapacityInOCU") is not None:
        out["max_search_capacity_in_ocu"] = float(data["maxSearchCapacityInOCU"])
    if data.get("minIndexingCapacityInOCU") is not None:
        out["min_indexing_capacity_in_ocu"] = float(data["minIndexingCapacityInOCU"])
    if data.get("minSearchCapacityInOCU") is not None:
        out["min_search_capacity_in_ocu"] = float(data["minSearchCapacityInOCU"])
    return out

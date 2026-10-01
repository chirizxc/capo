"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FailureSubCategoryCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.root_cause_cluster_list


class FailureSubCategoryCluster(TypedDict, closed=True):
    cluster_id: "int"
    """<p>The unique identifier of the failure subcategory cluster.</p>"""
    name: "str"
    """<p>The name of the failure subcategory.</p>"""
    description: "str"
    """<p>A description of the failure subcategory pattern.</p>"""
    affected_session_count: "int"
    """<p>The number of sessions affected by this failure subcategory.</p>"""
    root_causes: (
        "capo_bedrock_agentcore.types.root_cause_cluster_list.RootCauseClusterList"
    )
    """<p>The list of root cause clusters identified within this subcategory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureSubCategoryCluster) -> dict:
    out: dict = {}
    out["clusterId"] = value["cluster_id"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["affectedSessionCount"] = value["affected_session_count"]
    import capo_bedrock_agentcore.types.root_cause_cluster_list

    out["rootCauses"] = (
        capo_bedrock_agentcore.types.root_cause_cluster_list.serialize_json(
            value["root_causes"]
        )
    )
    return out


def deserialize_json(data: dict) -> FailureSubCategoryCluster:
    out: FailureSubCategoryCluster = {}  # type: ignore[typeddict-item]
    if data.get("clusterId") is not None:
        out["cluster_id"] = data["clusterId"]
    else:
        raise DeserializationError("FailureSubCategoryCluster.cluster_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FailureSubCategoryCluster.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("FailureSubCategoryCluster.description required")
    if data.get("affectedSessionCount") is not None:
        out["affected_session_count"] = data["affectedSessionCount"]
    else:
        raise DeserializationError(
            "FailureSubCategoryCluster.affected_session_count required"
        )
    if data.get("rootCauses") is not None:
        import capo_bedrock_agentcore.types.root_cause_cluster_list

        out["root_causes"] = (
            capo_bedrock_agentcore.types.root_cause_cluster_list.deserialize_json(
                data["rootCauses"]
            )
        )
    else:
        raise DeserializationError("FailureSubCategoryCluster.root_causes required")
    return out

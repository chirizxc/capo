"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolVnfcResourceInfoMetadata``."""

from typing_extensions import NotRequired, TypedDict


class GetSolVnfcResourceInfoMetadata(TypedDict, closed=True):
    node_group: NotRequired["str"]
    """<p>Information about the node group.</p>"""
    cluster: NotRequired["str"]
    """<p>Information about the cluster.</p>"""
    helm_chart: NotRequired["str"]
    """<p>Information about the helm chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolVnfcResourceInfoMetadata) -> dict:
    out: dict = {}
    if "node_group" in value:
        out["nodeGroup"] = value["node_group"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "helm_chart" in value:
        out["helmChart"] = value["helm_chart"]
    return out


def deserialize_json(data: dict) -> GetSolVnfcResourceInfoMetadata:
    out: GetSolVnfcResourceInfoMetadata = {}  # type: ignore[typeddict-item]
    if data.get("nodeGroup") is not None:
        out["node_group"] = data["nodeGroup"]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("helmChart") is not None:
        out["helm_chart"] = data["helmChart"]
    return out

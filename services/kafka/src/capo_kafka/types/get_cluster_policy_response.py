"""Generated from Smithy shape ``com.amazonaws.kafka#GetClusterPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class GetClusterPolicyResponse(TypedDict, closed=True):
    current_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The version of cluster policy.</p>"""
    policy: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The cluster policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterPolicyResponse) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetClusterPolicyResponse:
    out: GetClusterPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("currentVersion") is not None:
        out["current_version"] = data["currentVersion"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    return out

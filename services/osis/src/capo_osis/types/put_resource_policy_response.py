"""Generated from Smithy shape ``com.amazonaws.osis#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_arn
    import capo_osis.types.resource_policy


class PutResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: NotRequired["capo_osis.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    policy: NotRequired["capo_osis.types.resource_policy.ResourcePolicy"]
    """<p>The resource-based policy document that was attached to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out

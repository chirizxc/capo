"""Generated from Smithy shape ``com.amazonaws.lambda#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.resource_policy
    import capo_lambda.types.revision_id


class GetResourcePolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_lambda.types.resource_policy.ResourcePolicy"]
    """<p>The resource-based policy attached to the Lambda resource you specified.</p>"""
    revision_id: NotRequired["capo_lambda.types.revision_id.RevisionId"]
    """<p>The revision ID of the policy. Pass this value as the <code>RevisionId</code> in a <a>PutResourcePolicy</a> or <a>DeleteResourcePolicy</a> request. Doing so ensures the operation acts on the expected version of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out

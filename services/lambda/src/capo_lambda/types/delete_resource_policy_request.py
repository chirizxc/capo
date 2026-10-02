"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.policy_resource_arn
    import capo_lambda.types.revision_id


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_lambda.types.policy_resource_arn.PolicyResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda resource you want to delete the policy from. You can use a qualified or an unqualified ARN. The value must be a complete ARN, and the operation does not accept wildcard characters.</p>"""
    revision_id: NotRequired["capo_lambda.types.revision_id.RevisionId"]
    """<p>The revision ID that the existing policy must match for the deletion to proceed. If the revision ID doesn't match, the operation fails with a <code>PreconditionFailedException</code> error. To retrieve the current revision ID, use the <a>GetResourcePolicy</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out

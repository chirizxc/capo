"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.resource_arn
    import capo_bedrock_agent.types.revision_id


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base to remove the resource policy from.</p>"""
    expected_revision_id: NotRequired["capo_bedrock_agent.types.revision_id.RevisionId"]
    """<p>The expected revision identifier of the resource policy. Use this to prevent conflicts when multiple users update the same policy concurrently.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out

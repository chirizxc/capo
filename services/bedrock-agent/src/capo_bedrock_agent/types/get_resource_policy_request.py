"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.resource_arn


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base to retrieve the resource policy for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out

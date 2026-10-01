"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetVpcConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.vpc_configuration_id


class GetVpcConfigurationRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base that owns the VPC configuration.</p>"""
    vpc_configuration_id: (
        "capo_bedrock_agent.types.vpc_configuration_id.VpcConfigurationId"
    )
    """<p>The unique identifier of the VPC configuration to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVpcConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVpcConfigurationRequest:
    out: GetVpcConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

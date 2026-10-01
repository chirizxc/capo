"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteVpcConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.vpc_configuration_id


class DeleteVpcConfigurationRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base that owns the VPC configuration.</p>"""
    vpc_configuration_id: (
        "capo_bedrock_agent.types.vpc_configuration_id.VpcConfigurationId"
    )
    """<p>The unique identifier of the VPC configuration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVpcConfigurationRequest:
    out: DeleteVpcConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

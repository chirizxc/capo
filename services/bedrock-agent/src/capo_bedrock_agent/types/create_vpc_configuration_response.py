"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateVpcConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.vpc_configuration_id
    import capo_bedrock_agent.types.vpc_configuration_status


class CreateVpcConfigurationResponse(TypedDict, closed=True):
    vpc_configuration_id: (
        "capo_bedrock_agent.types.vpc_configuration_id.VpcConfigurationId"
    )
    """<p>The unique identifier of the VPC configuration that was created.</p>"""
    status: "capo_bedrock_agent.types.vpc_configuration_status.VpcConfigurationStatus"
    """<p>The current status of the VPC configuration. Immediately after creation this is <code>CREATING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcConfigurationResponse) -> dict:
    out: dict = {}
    out["vpcConfigurationId"] = value["vpc_configuration_id"]
    import capo_bedrock_agent.types.vpc_configuration_status

    out["status"] = capo_bedrock_agent.types.vpc_configuration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateVpcConfigurationResponse:
    out: CreateVpcConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("vpcConfigurationId") is not None:
        out["vpc_configuration_id"] = data["vpcConfigurationId"]
    else:
        raise DeserializationError(
            "CreateVpcConfigurationResponse.vpc_configuration_id required"
        )
    if data.get("status") is not None:
        import capo_bedrock_agent.types.vpc_configuration_status

        out["status"] = (
            capo_bedrock_agent.types.vpc_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateVpcConfigurationResponse.status required")
    return out

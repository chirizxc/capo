"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetVpcConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.vpc_configuration


class GetVpcConfigurationResponse(TypedDict, closed=True):
    vpc_configuration: "capo_bedrock_agent.types.vpc_configuration.VpcConfiguration"
    """<p>The VPC configuration, including its connection settings, resolution mode, and current lifecycle status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVpcConfigurationResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.vpc_configuration

    out["vpcConfiguration"] = capo_bedrock_agent.types.vpc_configuration.serialize_json(
        value["vpc_configuration"]
    )
    return out


def deserialize_json(data: dict) -> GetVpcConfigurationResponse:
    out: GetVpcConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("vpcConfiguration") is not None:
        import capo_bedrock_agent.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_bedrock_agent.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetVpcConfigurationResponse.vpc_configuration required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModelMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.provider_prefix


class ModelMapping(TypedDict, closed=True):
    provider_prefix: NotRequired[
        "capo_bedrock_agentcore_control.types.provider_prefix.ProviderPrefix"
    ]
    """<p>The provider prefix configuration used for model ID translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelMapping) -> dict:
    out: dict = {}
    if "provider_prefix" in value:
        import capo_bedrock_agentcore_control.types.provider_prefix

        out["providerPrefix"] = (
            capo_bedrock_agentcore_control.types.provider_prefix.serialize_json(
                value["provider_prefix"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModelMapping:
    out: ModelMapping = {}  # type: ignore[typeddict-item]
    if data.get("providerPrefix") is not None:
        import capo_bedrock_agentcore_control.types.provider_prefix

        out["provider_prefix"] = (
            capo_bedrock_agentcore_control.types.provider_prefix.deserialize_json(
                data["providerPrefix"]
            )
        )
    return out

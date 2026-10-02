"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrievePolicyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_guardrail_configuration


class AgenticRetrievePolicyConfiguration(TypedDict, closed=True):
    bedrock_guardrail_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_guardrail_configuration.AgenticRetrieveBedrockGuardrailConfiguration"
    ]
    """<p>Configuration for Bedrock guardrails to apply during retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrievePolicyConfiguration) -> dict:
    out: dict = {}
    if "bedrock_guardrail_configuration" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_guardrail_configuration

        out["bedrockGuardrailConfiguration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_guardrail_configuration.serialize_json(
                value["bedrock_guardrail_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrievePolicyConfiguration:
    out: AgenticRetrievePolicyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bedrockGuardrailConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_guardrail_configuration

        out["bedrock_guardrail_configuration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_guardrail_configuration.deserialize_json(
                data["bedrockGuardrailConfiguration"]
            )
        )
    return out

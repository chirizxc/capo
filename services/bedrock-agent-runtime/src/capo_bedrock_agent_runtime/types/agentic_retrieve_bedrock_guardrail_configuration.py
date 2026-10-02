"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveBedrockGuardrailConfiguration``."""

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError


class AgenticRetrieveBedrockGuardrailConfiguration(TypedDict, closed=True):
    guardrail_id: "str"
    """<p>The unique identifier of the guardrail.</p>"""
    guardrail_version: "str"
    """<p>The version of the guardrail to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveBedrockGuardrailConfiguration) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailVersion"] = value["guardrail_version"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveBedrockGuardrailConfiguration:
    out: AgenticRetrieveBedrockGuardrailConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("guardrailId") is not None:
        out["guardrail_id"] = data["guardrailId"]
    else:
        raise DeserializationError(
            "AgenticRetrieveBedrockGuardrailConfiguration.guardrail_id required"
        )
    if data.get("guardrailVersion") is not None:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        raise DeserializationError(
            "AgenticRetrieveBedrockGuardrailConfiguration.guardrail_version required"
        )
    return out

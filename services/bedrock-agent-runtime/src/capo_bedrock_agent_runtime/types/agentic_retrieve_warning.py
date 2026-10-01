"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveWarning``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_guardrail_warning
    import capo_bedrock_agent_runtime.types.agentic_retrieve_warning_message


class _AgenticRetrieveWarning_message(TypedDict, closed=True):
    message: "capo_bedrock_agent_runtime.types.agentic_retrieve_warning_message.AgenticRetrieveWarningMessage"


class _AgenticRetrieveWarning_guardrail(TypedDict, closed=True):
    guardrail: "capo_bedrock_agent_runtime.types.agentic_retrieve_guardrail_warning.AgenticRetrieveGuardrailWarning"


AgenticRetrieveWarning: TypeAlias = (
    _AgenticRetrieveWarning_message | _AgenticRetrieveWarning_guardrail
)


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveWarning) -> dict:
    if "message" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_warning_message

        return {
            "message": capo_bedrock_agent_runtime.types.agentic_retrieve_warning_message.serialize_json(
                value["message"]
            )
        }
    elif "guardrail" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_guardrail_warning

        return {
            "guardrail": capo_bedrock_agent_runtime.types.agentic_retrieve_guardrail_warning.serialize_json(
                value["guardrail"]
            )
        }
    else:
        raise SerializationError("AgenticRetrieveWarning: no variant present")


def deserialize_json(data: dict) -> AgenticRetrieveWarning:
    if data.get("message") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_warning_message

        return {
            "message": capo_bedrock_agent_runtime.types.agentic_retrieve_warning_message.deserialize_json(
                data["message"]
            )
        }
    elif data.get("guardrail") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_guardrail_warning

        return {
            "guardrail": capo_bedrock_agent_runtime.types.agentic_retrieve_guardrail_warning.deserialize_json(
                data["guardrail"]
            )
        }
    else:
        raise DeserializationError("AgenticRetrieveWarning: no recognized variant key")

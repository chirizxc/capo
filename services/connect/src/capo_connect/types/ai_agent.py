"""Generated from Smithy shape ``com.amazonaws.connect#AIAgent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.ai_agent_type
    import capo_connect.types.arn


class AIAgent(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the AI agent.</p>"""
    type: NotRequired["capo_connect.types.ai_agent_type.AIAgentType"]
    """<p>The type of the AI agent. The valid value is <code>THIRD_PARTY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIAgent) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        import capo_connect.types.ai_agent_type

        out["Type"] = capo_connect.types.ai_agent_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> AIAgent:
    out: AIAgent = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Type") is not None:
        import capo_connect.types.ai_agent_type

        out["type"] = capo_connect.types.ai_agent_type.deserialize_json(data["Type"])
    return out

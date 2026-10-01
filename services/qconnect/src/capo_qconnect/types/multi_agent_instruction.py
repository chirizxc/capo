"""Generated from Smithy shape ``com.amazonaws.qconnect#MultiAgentInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.multi_agent_example_list


class MultiAgentInstruction(TypedDict, closed=True):
    instruction: NotRequired["str"]
    """<p>The natural-language instruction that tells the Orchestration AI Agent when and how to engage the collaborator agent.</p>"""
    examples: NotRequired[
        "capo_qconnect.types.multi_agent_example_list.MultiAgentExampleList"
    ]
    """<p>Example interactions that illustrate when the Orchestration AI Agent should engage the collaborator agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiAgentInstruction) -> dict:
    out: dict = {}
    if "instruction" in value:
        out["instruction"] = value["instruction"]
    if "examples" in value:
        import capo_qconnect.types.multi_agent_example_list

        out["examples"] = capo_qconnect.types.multi_agent_example_list.serialize_json(
            value["examples"]
        )
    return out


def deserialize_json(data: dict) -> MultiAgentInstruction:
    out: MultiAgentInstruction = {}  # type: ignore[typeddict-item]
    if data.get("instruction") is not None:
        out["instruction"] = data["instruction"]
    if data.get("examples") is not None:
        import capo_qconnect.types.multi_agent_example_list

        out["examples"] = capo_qconnect.types.multi_agent_example_list.deserialize_json(
            data["examples"]
        )
    return out

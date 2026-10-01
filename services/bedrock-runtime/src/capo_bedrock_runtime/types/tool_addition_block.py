"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolAdditionBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_reference


class ToolAdditionBlock(TypedDict, closed=True):
    tool: "capo_bedrock_runtime.types.tool_reference.ToolReference"
    """<p>A reference to the tool to add to the available tool set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolAdditionBlock) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.tool_reference

    out["tool"] = capo_bedrock_runtime.types.tool_reference.serialize_json(
        value["tool"]
    )
    return out


def deserialize_json(data: dict) -> ToolAdditionBlock:
    out: ToolAdditionBlock = {}  # type: ignore[typeddict-item]
    if data.get("tool") is not None:
        import capo_bedrock_runtime.types.tool_reference

        out["tool"] = capo_bedrock_runtime.types.tool_reference.deserialize_json(
            data["tool"]
        )
    else:
        raise DeserializationError("ToolAdditionBlock.tool required")
    return out

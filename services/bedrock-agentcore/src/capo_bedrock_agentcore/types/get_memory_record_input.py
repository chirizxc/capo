"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetMemoryRecordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_record_id
    import capo_bedrock_agentcore.types.namespace


class GetMemoryRecordInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource containing the memory record.</p>"""
    memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The identifier of the memory record to retrieve.</p>"""
    namespace: NotRequired["capo_bedrock_agentcore.types.namespace.Namespace"]
    """<p>The namespace of the memory record to retrieve. This value is used for IAM condition key authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemoryRecordInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMemoryRecordInput:
    out: GetMemoryRecordInput = {}  # type: ignore[typeddict-item]
    return out

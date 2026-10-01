"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteHarnessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.harness_id


class DeleteHarnessRequest(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness to delete.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    delete_managed_memory: NotRequired["bool"]
    """<p>Whether to delete the managed memory on harness deletion. Default: true. If false, the memory is disassociated and becomes a regular customer-owned resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteHarnessRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteHarnessRequest:
    out: DeleteHarnessRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetHarnessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_version


class GetHarnessRequest(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness to retrieve.</p>"""
    harness_version: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
    ]
    """<p>Specific version of the harness to retrieve. If omitted, returns the current Harness configuration, including its status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHarnessRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetHarnessRequest:
    out: GetHarnessRequest = {}  # type: ignore[typeddict-item]
    return out

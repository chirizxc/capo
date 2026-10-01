"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetHarnessEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_endpoint_name
    import capo_bedrock_agentcore_control.types.harness_id


class GetHarnessEndpointRequest(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness that the endpoint belongs to.</p>"""
    endpoint_name: (
        "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName"
    )
    """<p>The name of the endpoint to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHarnessEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetHarnessEndpointRequest:
    out: GetHarnessEndpointRequest = {}  # type: ignore[typeddict-item]
    return out

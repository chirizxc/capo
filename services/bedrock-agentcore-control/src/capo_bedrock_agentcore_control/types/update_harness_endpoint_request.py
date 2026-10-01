"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateHarnessEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.harness_endpoint_description
    import capo_bedrock_agentcore_control.types.harness_endpoint_name
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_version


class UpdateHarnessEndpointRequest(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness that the endpoint belongs to.</p>"""
    endpoint_name: (
        "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName"
    )
    """<p>The name of the endpoint to update.</p>"""
    target_version: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
    ]
    """<p>The harness version that the endpoint points to. If not specified, the existing value is retained.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
    ]
    """<p>A description of the endpoint. If not specified, the existing value is retained.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHarnessEndpointRequest) -> dict:
    out: dict = {}
    if "target_version" in value:
        out["targetVersion"] = value["target_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateHarnessEndpointRequest:
    out: UpdateHarnessEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetVersion") is not None:
        out["target_version"] = data["targetVersion"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

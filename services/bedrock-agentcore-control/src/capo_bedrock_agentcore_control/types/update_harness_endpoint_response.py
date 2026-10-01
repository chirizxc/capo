"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateHarnessEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_endpoint


class UpdateHarnessEndpointResponse(TypedDict, closed=True):
    endpoint: "capo_bedrock_agentcore_control.types.harness_endpoint.HarnessEndpoint"
    """<p>The updated endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHarnessEndpointResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.harness_endpoint

    out["endpoint"] = (
        capo_bedrock_agentcore_control.types.harness_endpoint.serialize_json(
            value["endpoint"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateHarnessEndpointResponse:
    out: UpdateHarnessEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        import capo_bedrock_agentcore_control.types.harness_endpoint

        out["endpoint"] = (
            capo_bedrock_agentcore_control.types.harness_endpoint.deserialize_json(
                data["endpoint"]
            )
        )
    else:
        raise DeserializationError("UpdateHarnessEndpointResponse.endpoint required")
    return out

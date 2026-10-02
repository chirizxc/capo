"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_identifier
    import capo_bedrock_agent.types.included_data


class GetFlowRequest(TypedDict, closed=True):
    flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow.</p>"""
    included_data: NotRequired["capo_bedrock_agent.types.included_data.IncludedData"]
    """<p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFlowRequest:
    out: GetFlowRequest = {}  # type: ignore[typeddict-item]
    return out

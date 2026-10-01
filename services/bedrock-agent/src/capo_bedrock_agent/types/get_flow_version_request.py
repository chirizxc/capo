"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetFlowVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_identifier
    import capo_bedrock_agent.types.included_data
    import capo_bedrock_agent.types.numerical_version


class GetFlowVersionRequest(TypedDict, closed=True):
    flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow for which to get information.</p>"""
    flow_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version of the flow for which to get information.</p>"""
    included_data: NotRequired["capo_bedrock_agent.types.included_data.IncludedData"]
    """<p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFlowVersionRequest:
    out: GetFlowVersionRequest = {}  # type: ignore[typeddict-item]
    return out

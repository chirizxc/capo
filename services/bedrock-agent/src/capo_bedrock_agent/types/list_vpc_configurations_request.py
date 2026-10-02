"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListVpcConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.vpc_configuration_status


class ListVpcConfigurationsRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base whose VPC configurations you want to list.</p>"""
    status_filter: NotRequired[
        "capo_bedrock_agent.types.vpc_configuration_status.VpcConfigurationStatus"
    ]
    """<p>The status to filter the results by. Only VPC configurations with the specified status are returned.</p>"""
    max_results: NotRequired["capo_bedrock_agent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If more results are available, the response returns a <code>nextToken</code>.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>A pagination token to retrieve the next page of results, returned in a previous response when more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVpcConfigurationsRequest:
    out: ListVpcConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListWorkflowsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListWorkflowsRequest(TypedDict, closed=True):
    max_results: "int"
    """<p>The maximum number of workflows you want to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflows</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkflowsRequest) -> dict:
    out: dict = {}
    out["MaxResults"] = value.get("max_results", 20)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkflowsRequest:
    out: ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 20
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.acm#ListAcmeEndpointsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListAcmeEndpointsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token for pagination.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcmeEndpointsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcmeEndpointsRequest:
    out: ListAcmeEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out

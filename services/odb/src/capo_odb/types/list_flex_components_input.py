"""Generated from Smithy shape ``com.amazonaws.odb#ListFlexComponentsInput``."""

from typing_extensions import NotRequired, TypedDict


class ListFlexComponentsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    shape: NotRequired["str"]
    """<p>The shape to return flex components for. For a list of valid shapes, use the <code>ListDbSystemShapes</code> operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFlexComponentsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "shape" in value:
        out["shape"] = value["shape"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFlexComponentsInput:
    out: ListFlexComponentsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    return out

"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListStateTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token


class ListStateTemplatesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""
    max_results: NotRequired["capo_iotfleetwise.types.max_results.maxResults"]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""
    list_response_scope: NotRequired[
        "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
    ]
    """<p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: state template ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStateTemplatesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "list_response_scope" in value:
        import capo_iotfleetwise.types.list_response_scope

        out["listResponseScope"] = (
            capo_iotfleetwise.types.list_response_scope.serialize_aws_json_1_0(
                value["list_response_scope"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStateTemplatesRequest:
    out: ListStateTemplatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("listResponseScope") is not None:
        import capo_iotfleetwise.types.list_response_scope

        out["list_response_scope"] = (
            capo_iotfleetwise.types.list_response_scope.deserialize_aws_json_1_0(
                data["listResponseScope"]
            )
        )
    return out

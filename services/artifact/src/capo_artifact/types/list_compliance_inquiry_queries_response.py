"""Generated from Smithy shape ``com.amazonaws.artifact#ListComplianceInquiryQueriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.next_token_attribute
    import capo_artifact.types.queries_list


class ListComplianceInquiryQueriesResponse(TypedDict, closed=True):
    queries: NotRequired["capo_artifact.types.queries_list.QueriesList"]
    """<p>List of compliance query summaries.</p>"""
    next_token: NotRequired[
        "capo_artifact.types.next_token_attribute.NextTokenAttribute"
    ]
    """<p>Pagination token to request the next page of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComplianceInquiryQueriesResponse) -> dict:
    out: dict = {}
    if "queries" in value:
        import capo_artifact.types.queries_list

        out["queries"] = capo_artifact.types.queries_list.serialize_json(
            value["queries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComplianceInquiryQueriesResponse:
    out: ListComplianceInquiryQueriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("queries") is not None:
        import capo_artifact.types.queries_list

        out["queries"] = capo_artifact.types.queries_list.deserialize_json(
            data["queries"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

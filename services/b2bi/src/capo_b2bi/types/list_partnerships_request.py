"""Generated from Smithy shape ``com.amazonaws.b2bi#ListPartnershipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.max_results
    import capo_b2bi.types.page_token
    import capo_b2bi.types.profile_id


class ListPartnershipsRequest(TypedDict, closed=True):
    profile_id: NotRequired["capo_b2bi.types.profile_id.ProfileId"]
    """<p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>"""
    next_token: NotRequired["capo_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""
    max_results: NotRequired["capo_b2bi.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of capabilities to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPartnershipsRequest) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["profileId"] = value["profile_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPartnershipsRequest:
    out: ListPartnershipsRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

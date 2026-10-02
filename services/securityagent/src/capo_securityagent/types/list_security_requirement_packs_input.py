"""Generated from Smithy shape ``com.amazonaws.securityagent#ListSecurityRequirementPacksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.list_security_requirement_pack_filter
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token


class ListSecurityRequirementPacksInput(TypedDict, closed=True):
    filter: NotRequired[
        "capo_securityagent.types.list_security_requirement_pack_filter.ListSecurityRequirementPackFilter"
    ]
    """<p>The filter criteria for listing security requirement packs.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>The pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityRequirementPacksInput) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_securityagent.types.list_security_requirement_pack_filter

        out["filter"] = (
            capo_securityagent.types.list_security_requirement_pack_filter.serialize_json(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListSecurityRequirementPacksInput:
    out: ListSecurityRequirementPacksInput = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_securityagent.types.list_security_requirement_pack_filter

        out["filter"] = (
            capo_securityagent.types.list_security_requirement_pack_filter.deserialize_json(
                data["filter"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

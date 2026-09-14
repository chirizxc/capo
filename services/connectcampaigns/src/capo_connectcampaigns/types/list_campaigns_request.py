"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#ListCampaignsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_filters
    import capo_connectcampaigns.types.max_results
    import capo_connectcampaigns.types.next_token


class ListCampaignsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_connectcampaigns.types.max_results.MaxResults"]
    next_token: NotRequired["capo_connectcampaigns.types.next_token.NextToken"]
    filters: NotRequired["capo_connectcampaigns.types.campaign_filters.CampaignFilters"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCampaignsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_connectcampaigns.types.campaign_filters

        out["filters"] = capo_connectcampaigns.types.campaign_filters.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListCampaignsRequest:
    out: ListCampaignsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_connectcampaigns.types.campaign_filters

        out["filters"] = capo_connectcampaigns.types.campaign_filters.deserialize_json(
            data["filters"]
        )
    return out

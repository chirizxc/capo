"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageScanFindingAggregationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter
    import capo_imagebuilder.types.pagination_token


class ListImageScanFindingAggregationsRequest(TypedDict, closed=True):
    filter: NotRequired["capo_imagebuilder.types.filter.Filter"]
    """<p>A filter name and value pair that determines the type of aggregation that Image Builder returns. Use one of the following filter names:</p> <ul> <li> <p> <code>imageBuildVersionArn</code> </p> </li> <li> <p> <code>imagePipelineArn</code> </p> </li> <li> <p> <code>vulnerabilityId</code> </p> </li> </ul> <p>If you don't specify a filter, Image Builder returns an aggregation for your account.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageScanFindingAggregationsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_imagebuilder.types.filter

        out["filter"] = capo_imagebuilder.types.filter.serialize_json(value["filter"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageScanFindingAggregationsRequest:
    out: ListImageScanFindingAggregationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_imagebuilder.types.filter

        out["filter"] = capo_imagebuilder.types.filter.deserialize_json(data["filter"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

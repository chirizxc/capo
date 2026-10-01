"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListSearchesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.list_searches_filters
    import capo_iotsitewise.types.list_searches_request_max_results_integer
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.workspace_name


class ListSearchesRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace whose searches are listed.</p>"""
    max_results: NotRequired[
        "capo_iotsitewise.types.list_searches_request_max_results_integer.ListSearchesRequestMaxResultsInteger"
    ]
    """<p>The maximum number of searches to return in a single page. Valid range is 1 to 1,000; if omitted, a service-defined default is used.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The pagination token returned by a previous ListSearches call. Provide it to retrieve the next page; omit it to retrieve the first page.</p>"""
    list_searches_filters: NotRequired[
        "capo_iotsitewise.types.list_searches_filters.ListSearchesFilters"
    ]
    """<p>Optional filters that restrict which searches are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "list_searches_filters" in value:
        import capo_iotsitewise.types.list_searches_filters

        out["listSearchesFilters"] = (
            capo_iotsitewise.types.list_searches_filters.serialize_json(
                value["list_searches_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSearchesRequest:
    out: ListSearchesRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("listSearchesFilters") is not None:
        import capo_iotsitewise.types.list_searches_filters

        out["list_searches_filters"] = (
            capo_iotsitewise.types.list_searches_filters.deserialize_json(
                data["listSearchesFilters"]
            )
        )
    return out

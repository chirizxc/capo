"""Generated from Smithy shape ``com.amazonaws.glue#SearchAssetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.search_filter_clause
    import capo_glue.types.search_max_results
    import capo_glue.types.search_next_token
    import capo_glue.types.search_sort
    import capo_glue.types.search_text


class SearchAssetsInput(TypedDict, closed=True):
    search_text: NotRequired["capo_glue.types.search_text.SearchText"]
    """<p>The text to search for. At least one of <code>searchText</code> or <code>filterClause</code> must be provided.</p>"""
    max_results: NotRequired["capo_glue.types.search_max_results.SearchMaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_glue.types.search_next_token.SearchNextToken"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    sort: NotRequired["capo_glue.types.search_sort.SearchSort"]
    """<p>The sort criteria for the search results.</p>"""
    filter_clause: NotRequired[
        "capo_glue.types.search_filter_clause.SearchFilterClause"
    ]
    """<p>The filter clause to apply to the search. Supports nested AND/OR logic with attribute-level and map-level filters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchAssetsInput) -> dict:
    out: dict = {}
    if "search_text" in value:
        out["SearchText"] = value["search_text"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort" in value:
        import capo_glue.types.search_sort

        out["Sort"] = capo_glue.types.search_sort.serialize_aws_json_1_1(value["sort"])
    if "filter_clause" in value:
        import capo_glue.types.search_filter_clause

        out["FilterClause"] = (
            capo_glue.types.search_filter_clause.serialize_aws_json_1_1(
                value["filter_clause"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchAssetsInput:
    out: SearchAssetsInput = {}  # type: ignore[typeddict-item]
    if data.get("SearchText") is not None:
        out["search_text"] = data["SearchText"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Sort") is not None:
        import capo_glue.types.search_sort

        out["sort"] = capo_glue.types.search_sort.deserialize_aws_json_1_1(data["Sort"])
    if data.get("FilterClause") is not None:
        import capo_glue.types.search_filter_clause

        out["filter_clause"] = (
            capo_glue.types.search_filter_clause.deserialize_aws_json_1_1(
                data["FilterClause"]
            )
        )
    return out

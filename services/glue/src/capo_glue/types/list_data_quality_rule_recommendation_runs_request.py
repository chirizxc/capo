"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityRuleRecommendationRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_rule_recommendation_run_filter
    import capo_glue.types.page_size
    import capo_glue.types.pagination_token
    import capo_glue.types.tags_map


class ListDataQualityRuleRecommendationRunsRequest(TypedDict, closed=True):
    filter: NotRequired[
        "capo_glue.types.data_quality_rule_recommendation_run_filter.DataQualityRuleRecommendationRunFilter"
    ]
    """<p>The filter criteria.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A paginated token to offset the results.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>A list of key-value pair tags to filter recommendation runs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityRuleRecommendationRunsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_glue.types.data_quality_rule_recommendation_run_filter

        out["Filter"] = (
            capo_glue.types.data_quality_rule_recommendation_run_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListDataQualityRuleRecommendationRunsRequest:
    out: ListDataQualityRuleRecommendationRunsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_glue.types.data_quality_rule_recommendation_run_filter

        out["filter"] = (
            capo_glue.types.data_quality_rule_recommendation_run_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out

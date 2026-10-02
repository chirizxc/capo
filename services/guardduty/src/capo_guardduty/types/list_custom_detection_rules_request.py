"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCustomDetectionRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_filter_list
    import capo_guardduty.types.detection_rule_max_results
    import capo_guardduty.types.string


class ListCustomDetectionRulesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
    ]
    """<p>The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A pagination token from a previous response. Use this token to retrieve the next page of results.</p>"""
    filters: NotRequired[
        "capo_guardduty.types.detection_rule_filter_list.DetectionRuleFilterList"
    ]
    """<p>A list of filter criteria to apply when listing custom detection rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomDetectionRulesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_guardduty.types.detection_rule_filter_list

        out["filters"] = capo_guardduty.types.detection_rule_filter_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListCustomDetectionRulesRequest:
    out: ListCustomDetectionRulesRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_guardduty.types.detection_rule_filter_list

        out["filters"] = (
            capo_guardduty.types.detection_rule_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out

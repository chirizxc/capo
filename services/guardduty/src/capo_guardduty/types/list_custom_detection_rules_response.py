"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCustomDetectionRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.rule_summary_list
    import capo_guardduty.types.string


class ListCustomDetectionRulesResponse(TypedDict, closed=True):
    rules: NotRequired["capo_guardduty.types.rule_summary_list.RuleSummaryList"]
    """<p>A list of custom detection rule summaries.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A pagination token to retrieve the next page of results. If this field is empty, there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomDetectionRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_guardduty.types.rule_summary_list

        out["rules"] = capo_guardduty.types.rule_summary_list.serialize_json(
            value["rules"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomDetectionRulesResponse:
    out: ListCustomDetectionRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("rules") is not None:
        import capo_guardduty.types.rule_summary_list

        out["rules"] = capo_guardduty.types.rule_summary_list.deserialize_json(
            data["rules"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCustomDetectionRuleAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_summary_list
    import capo_guardduty.types.string


class ListCustomDetectionRuleAssociationsResponse(TypedDict, closed=True):
    rule_associations: NotRequired[
        "capo_guardduty.types.association_summary_list.AssociationSummaryList"
    ]
    """<p>A list of custom detection rule association summaries.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A pagination token to retrieve the next page of results. If this field is empty, there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomDetectionRuleAssociationsResponse) -> dict:
    out: dict = {}
    if "rule_associations" in value:
        import capo_guardduty.types.association_summary_list

        out["ruleAssociations"] = (
            capo_guardduty.types.association_summary_list.serialize_json(
                value["rule_associations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomDetectionRuleAssociationsResponse:
    out: ListCustomDetectionRuleAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleAssociations") is not None:
        import capo_guardduty.types.association_summary_list

        out["rule_associations"] = (
            capo_guardduty.types.association_summary_list.deserialize_json(
                data["ruleAssociations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

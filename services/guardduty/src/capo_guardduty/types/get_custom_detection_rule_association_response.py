"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCustomDetectionRuleAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_detail
    import capo_guardduty.types.tag_map


class GetCustomDetectionRuleAssociationResponse(TypedDict, closed=True):
    rule_association: NotRequired[
        "capo_guardduty.types.association_detail.AssociationDetail"
    ]
    """<p>The details of the custom detection rule association.</p>"""
    tags: NotRequired["capo_guardduty.types.tag_map.TagMap"]
    """<p>The tags associated with the custom detection rule association resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomDetectionRuleAssociationResponse) -> dict:
    out: dict = {}
    if "rule_association" in value:
        import capo_guardduty.types.association_detail

        out["ruleAssociation"] = capo_guardduty.types.association_detail.serialize_json(
            value["rule_association"]
        )
    if "tags" in value:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCustomDetectionRuleAssociationResponse:
    out: GetCustomDetectionRuleAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleAssociation") is not None:
        import capo_guardduty.types.association_detail

        out["rule_association"] = (
            capo_guardduty.types.association_detail.deserialize_json(
                data["ruleAssociation"]
            )
        )
    if data.get("tags") is not None:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.deserialize_json(data["tags"])
    return out

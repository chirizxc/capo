"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateCustomDetectionRuleAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_detail


class CreateCustomDetectionRuleAssociationResponse(TypedDict, closed=True):
    rule_association: NotRequired[
        "capo_guardduty.types.association_detail.AssociationDetail"
    ]
    """<p>The details of the newly created custom detection rule association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomDetectionRuleAssociationResponse) -> dict:
    out: dict = {}
    if "rule_association" in value:
        import capo_guardduty.types.association_detail

        out["ruleAssociation"] = capo_guardduty.types.association_detail.serialize_json(
            value["rule_association"]
        )
    return out


def deserialize_json(data: dict) -> CreateCustomDetectionRuleAssociationResponse:
    out: CreateCustomDetectionRuleAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleAssociation") is not None:
        import capo_guardduty.types.association_detail

        out["rule_association"] = (
            capo_guardduty.types.association_detail.deserialize_json(
                data["ruleAssociation"]
            )
        )
    return out

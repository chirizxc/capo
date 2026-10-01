"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCustomDetectionRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.rule_detail


class GetCustomDetectionRuleResponse(TypedDict, closed=True):
    rule: NotRequired["capo_guardduty.types.rule_detail.RuleDetail"]
    """<p>The details of the custom detection rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomDetectionRuleResponse) -> dict:
    out: dict = {}
    if "rule" in value:
        import capo_guardduty.types.rule_detail

        out["rule"] = capo_guardduty.types.rule_detail.serialize_json(value["rule"])
    return out


def deserialize_json(data: dict) -> GetCustomDetectionRuleResponse:
    out: GetCustomDetectionRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("rule") is not None:
        import capo_guardduty.types.rule_detail

        out["rule"] = capo_guardduty.types.rule_detail.deserialize_json(data["rule"])
    return out

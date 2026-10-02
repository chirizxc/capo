"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCustomDetectionRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.rule_id


class GetCustomDetectionRuleRequest(TypedDict, closed=True):
    rule_id: "capo_guardduty.types.rule_id.RuleId"
    """<p>The unique identifier for the custom detection rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomDetectionRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCustomDetectionRuleRequest:
    out: GetCustomDetectionRuleRequest = {}  # type: ignore[typeddict-item]
    return out

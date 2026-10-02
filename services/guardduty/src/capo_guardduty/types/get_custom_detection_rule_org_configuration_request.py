"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCustomDetectionRuleOrgConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_mode
    import capo_guardduty.types.rule_id


class GetCustomDetectionRuleOrgConfigurationRequest(TypedDict, closed=True):
    rule_id: "capo_guardduty.types.rule_id.RuleId"
    """<p>The unique identifier for the custom detection rule.</p>"""
    mode: NotRequired["capo_guardduty.types.association_mode.AssociationMode"]
    """<p>The execution mode of the organization configuration to retrieve. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomDetectionRuleOrgConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCustomDetectionRuleOrgConfigurationRequest:
    out: GetCustomDetectionRuleOrgConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

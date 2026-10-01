"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCustomDetectionRuleOrgConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_org_configuration


class GetCustomDetectionRuleOrgConfigurationResponse(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_guardduty.types.detection_rule_org_configuration.DetectionRuleOrgConfiguration"
    ]
    """<p>The details of the organization configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomDetectionRuleOrgConfigurationResponse) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_guardduty.types.detection_rule_org_configuration

        out["configuration"] = (
            capo_guardduty.types.detection_rule_org_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCustomDetectionRuleOrgConfigurationResponse:
    out: GetCustomDetectionRuleOrgConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_guardduty.types.detection_rule_org_configuration

        out["configuration"] = (
            capo_guardduty.types.detection_rule_org_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out

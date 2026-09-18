"""Generated from Smithy shape ``com.amazonaws.iot#AuditNotificationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.enabled
    import capo_iot.types.role_arn
    import capo_iot.types.target_arn


class AuditNotificationTarget(TypedDict, closed=True):
    target_arn: NotRequired["capo_iot.types.target_arn.TargetArn"]
    """<p>The ARN of the target (SNS topic) to which audit notifications are sent.</p>"""
    role_arn: NotRequired["capo_iot.types.role_arn.RoleArn"]
    """<p>The ARN of the role that grants permission to send notifications to the target.</p>"""
    enabled: "capo_iot.types.enabled.Enabled"
    """<p>True if notifications to the target are enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditNotificationTarget) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> AuditNotificationTarget:
    out: AuditNotificationTarget = {}  # type: ignore[typeddict-item]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out

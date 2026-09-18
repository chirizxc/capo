"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanBackupPlanDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list
    import capo_securityhub.types.aws_backup_backup_plan_rule_list
    import capo_securityhub.types.non_empty_string


class AwsBackupBackupPlanBackupPlanDetails(TypedDict, closed=True):
    backup_plan_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The display name of a backup plan. </p>"""
    advanced_backup_settings: NotRequired[
        "capo_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list.AwsBackupBackupPlanAdvancedBackupSettingsList"
    ]
    """<p>A list of backup options for each resource type. </p>"""
    backup_plan_rule: NotRequired[
        "capo_securityhub.types.aws_backup_backup_plan_rule_list.AwsBackupBackupPlanRuleList"
    ]
    """<p>An array of <code>BackupRule</code> objects, each of which specifies a scheduled task that is used to back up a selection of resources. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanBackupPlanDetails) -> dict:
    out: dict = {}
    if "backup_plan_name" in value:
        out["BackupPlanName"] = value["backup_plan_name"]
    if "advanced_backup_settings" in value:
        import capo_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list

        out["AdvancedBackupSettings"] = (
            capo_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list.serialize_json(
                value["advanced_backup_settings"]
            )
        )
    if "backup_plan_rule" in value:
        import capo_securityhub.types.aws_backup_backup_plan_rule_list

        out["BackupPlanRule"] = (
            capo_securityhub.types.aws_backup_backup_plan_rule_list.serialize_json(
                value["backup_plan_rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsBackupBackupPlanBackupPlanDetails:
    out: AwsBackupBackupPlanBackupPlanDetails = {}  # type: ignore[typeddict-item]
    if data.get("BackupPlanName") is not None:
        out["backup_plan_name"] = data["BackupPlanName"]
    if data.get("AdvancedBackupSettings") is not None:
        import capo_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list

        out["advanced_backup_settings"] = (
            capo_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list.deserialize_json(
                data["AdvancedBackupSettings"]
            )
        )
    if data.get("BackupPlanRule") is not None:
        import capo_securityhub.types.aws_backup_backup_plan_rule_list

        out["backup_plan_rule"] = (
            capo_securityhub.types.aws_backup_backup_plan_rule_list.deserialize_json(
                data["BackupPlanRule"]
            )
        )
    return out

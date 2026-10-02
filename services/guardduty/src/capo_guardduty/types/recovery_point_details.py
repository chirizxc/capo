"""Generated from Smithy shape ``com.amazonaws.guardduty#RecoveryPointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.scan_configuration_continuous_scan_details
    import capo_guardduty.types.string


class RecoveryPointDetails(TypedDict, closed=True):
    recovery_point_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the recovery point.</p>"""
    backup_vault_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the backup vault containing the recovery point.</p>"""
    continuous_scan_details: NotRequired[
        "capo_guardduty.types.scan_configuration_continuous_scan_details.ScanConfigurationContinuousScanDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointDetails) -> dict:
    out: dict = {}
    if "recovery_point_arn" in value:
        out["recoveryPointArn"] = value["recovery_point_arn"]
    if "backup_vault_name" in value:
        out["backupVaultName"] = value["backup_vault_name"]
    if "continuous_scan_details" in value:
        import capo_guardduty.types.scan_configuration_continuous_scan_details

        out["continuousScanDetails"] = (
            capo_guardduty.types.scan_configuration_continuous_scan_details.serialize_json(
                value["continuous_scan_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecoveryPointDetails:
    out: RecoveryPointDetails = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPointArn") is not None:
        out["recovery_point_arn"] = data["recoveryPointArn"]
    if data.get("backupVaultName") is not None:
        out["backup_vault_name"] = data["backupVaultName"]
    if data.get("continuousScanDetails") is not None:
        import capo_guardduty.types.scan_configuration_continuous_scan_details

        out["continuous_scan_details"] = (
            capo_guardduty.types.scan_configuration_continuous_scan_details.deserialize_json(
                data["continuousScanDetails"]
            )
        )
    return out

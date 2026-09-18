"""Generated from Smithy shape ``com.amazonaws.odb#LongTermBackupSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.repeat_cadence


class LongTermBackupSchedule(TypedDict, closed=True):
    is_disabled: NotRequired["bool"]
    """<p>Indicates whether the long-term backup schedule is disabled.</p>"""
    repeat_cadence: NotRequired["capo_odb.types.repeat_cadence.RepeatCadence"]
    """<p>The cadence at which long-term backups are taken.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for long-term backups.</p>"""
    time_of_backup: NotRequired["datetime.datetime"]
    """<p>The date and time at which the long-term backup is taken.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LongTermBackupSchedule) -> dict:
    out: dict = {}
    if "is_disabled" in value:
        out["isDisabled"] = value["is_disabled"]
    if "repeat_cadence" in value:
        import capo_odb.types.repeat_cadence

        out["repeatCadence"] = capo_odb.types.repeat_cadence.serialize_aws_json_1_0(
            value["repeat_cadence"]
        )
    if "retention_period_in_days" in value:
        out["retentionPeriodInDays"] = value["retention_period_in_days"]
    if "time_of_backup" in value:
        import capo_odb._protocol.serialize

        out["timeOfBackup"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_backup"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LongTermBackupSchedule:
    out: LongTermBackupSchedule = {}  # type: ignore[typeddict-item]
    if data.get("isDisabled") is not None:
        out["is_disabled"] = data["isDisabled"]
    if data.get("repeatCadence") is not None:
        import capo_odb.types.repeat_cadence

        out["repeat_cadence"] = capo_odb.types.repeat_cadence.deserialize_aws_json_1_0(
            data["repeatCadence"]
        )
    if data.get("retentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["retentionPeriodInDays"]
    if data.get("timeOfBackup") is not None:
        import datetime

        out["time_of_backup"] = datetime.datetime.fromisoformat(
            data["timeOfBackup"].replace("Z", "+00:00")
        )
    return out

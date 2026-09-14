"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftLineageSyncConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.lineage_sync_schedule


class RedshiftLineageSyncConfigurationOutput(TypedDict, closed=True):
    lineage_job_id: NotRequired["str"]
    """<p>The lineage job ID of the Amaon Redshift lineage sync configuration.</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether the Amaon Redshift lineage sync configuration is enabled.</p>"""
    schedule: NotRequired[
        "capo_datazone.types.lineage_sync_schedule.LineageSyncSchedule"
    ]
    """<p>The schedule of teh Amaon Redshift lineage sync configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftLineageSyncConfigurationOutput) -> dict:
    out: dict = {}
    if "lineage_job_id" in value:
        out["lineageJobId"] = value["lineage_job_id"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "schedule" in value:
        import capo_datazone.types.lineage_sync_schedule

        out["schedule"] = capo_datazone.types.lineage_sync_schedule.serialize_json(
            value["schedule"]
        )
    return out


def deserialize_json(data: dict) -> RedshiftLineageSyncConfigurationOutput:
    out: RedshiftLineageSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("lineageJobId") is not None:
        out["lineage_job_id"] = data["lineageJobId"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("schedule") is not None:
        import capo_datazone.types.lineage_sync_schedule

        out["schedule"] = capo_datazone.types.lineage_sync_schedule.deserialize_json(
            data["schedule"]
        )
    return out

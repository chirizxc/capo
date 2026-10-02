"""Generated from Smithy shape ``com.amazonaws.datazone#LineageSyncOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.lineage_sync_schedule_cron_string
    import capo_datazone.types.timezone


class LineageSyncOutput(TypedDict, closed=True):
    lineage_job_id: NotRequired["str"]
    """<p>The ID of the lineage sync job.</p>"""
    timezone: NotRequired["capo_datazone.types.timezone.Timezone"]
    """<p>The timezone of the lineage sync schedule.</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether lineage sync is enabled.</p>"""
    schedule: NotRequired[
        "capo_datazone.types.lineage_sync_schedule_cron_string.LineageSyncScheduleCronString"
    ]
    """<p>The schedule of the lineage sync.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageSyncOutput) -> dict:
    out: dict = {}
    if "lineage_job_id" in value:
        out["lineageJobId"] = value["lineage_job_id"]
    if "timezone" in value:
        import capo_datazone.types.timezone

        out["timezone"] = capo_datazone.types.timezone.serialize_json(value["timezone"])
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "schedule" in value:
        out["schedule"] = value["schedule"]
    return out


def deserialize_json(data: dict) -> LineageSyncOutput:
    out: LineageSyncOutput = {}  # type: ignore[typeddict-item]
    if data.get("lineageJobId") is not None:
        out["lineage_job_id"] = data["lineageJobId"]
    if data.get("timezone") is not None:
        import capo_datazone.types.timezone

        out["timezone"] = capo_datazone.types.timezone.deserialize_json(
            data["timezone"]
        )
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("schedule") is not None:
        out["schedule"] = data["schedule"]
    return out

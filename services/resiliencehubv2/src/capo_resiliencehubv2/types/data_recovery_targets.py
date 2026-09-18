"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DataRecoveryTargets``."""

from typing_extensions import NotRequired, TypedDict


class DataRecoveryTargets(TypedDict, closed=True):
    time_between_backups_in_minutes: NotRequired["int"]
    """<p>The target time between backups, in minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataRecoveryTargets) -> dict:
    out: dict = {}
    if "time_between_backups_in_minutes" in value:
        out["timeBetweenBackupsInMinutes"] = value["time_between_backups_in_minutes"]
    return out


def deserialize_json(data: dict) -> DataRecoveryTargets:
    out: DataRecoveryTargets = {}  # type: ignore[typeddict-item]
    if data.get("timeBetweenBackupsInMinutes") is not None:
        out["time_between_backups_in_minutes"] = data["timeBetweenBackupsInMinutes"]
    return out

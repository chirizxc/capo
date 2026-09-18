"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryLifeCycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_drs.types.job_id
    import capo_drs.types.recovery_result


class RecoveryLifeCycle(TypedDict, closed=True):
    api_call_date_time: NotRequired["datetime.datetime"]
    """<p>The date and time the last Source Network recovery was initiated.</p>"""
    job_id: NotRequired["capo_drs.types.job_id.JobID"]
    """<p>The ID of the Job that was used to last recover the Source Network.</p>"""
    last_recovery_result: NotRequired["capo_drs.types.recovery_result.RecoveryResult"]
    """<p>The status of the last recovery status of this Source Network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryLifeCycle) -> dict:
    out: dict = {}
    if "api_call_date_time" in value:
        import capo_drs._protocol.serialize

        out["apiCallDateTime"] = capo_drs._protocol.serialize.fmt_date_time(
            value["api_call_date_time"]
        )
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "last_recovery_result" in value:
        out["lastRecoveryResult"] = value["last_recovery_result"]
    return out


def deserialize_json(data: dict) -> RecoveryLifeCycle:
    out: RecoveryLifeCycle = {}  # type: ignore[typeddict-item]
    if data.get("apiCallDateTime") is not None:
        import datetime

        out["api_call_date_time"] = datetime.datetime.fromisoformat(
            data["apiCallDateTime"].replace("Z", "+00:00")
        )
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    if data.get("lastRecoveryResult") is not None:
        out["last_recovery_result"] = data["lastRecoveryResult"]
    return out

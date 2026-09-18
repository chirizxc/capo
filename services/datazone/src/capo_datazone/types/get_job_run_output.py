"""Generated from Smithy shape ``com.amazonaws.datazone#GetJobRunOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.domain_id
    import capo_datazone.types.job_run_details
    import capo_datazone.types.job_run_error
    import capo_datazone.types.job_run_mode
    import capo_datazone.types.job_run_status
    import capo_datazone.types.job_type


class GetJobRunOutput(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the domain.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the job run.</p>"""
    job_id: NotRequired["str"]
    """<p>The ID of the job run.</p>"""
    job_type: NotRequired["capo_datazone.types.job_type.JobType"]
    """<p>The type of the job run.</p>"""
    run_mode: NotRequired["capo_datazone.types.job_run_mode.JobRunMode"]
    """<p>The mode of the job run.</p>"""
    details: NotRequired["capo_datazone.types.job_run_details.JobRunDetails"]
    """<p>The details of the job run.</p>"""
    status: NotRequired["capo_datazone.types.job_run_status.JobRunStatus"]
    """<p>The status of the job run.</p>"""
    error: NotRequired["capo_datazone.types.job_run_error.JobRunError"]
    """<p>The error generated if the action is not completed successfully.</p>"""
    created_by: NotRequired["str"]
    """<p>The user who created the job run.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the job run was created.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the job run started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the job run ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRunOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_type" in value:
        import capo_datazone.types.job_type

        out["jobType"] = capo_datazone.types.job_type.serialize_json(value["job_type"])
    if "run_mode" in value:
        import capo_datazone.types.job_run_mode

        out["runMode"] = capo_datazone.types.job_run_mode.serialize_json(
            value["run_mode"]
        )
    if "details" in value:
        import capo_datazone.types.job_run_details

        out["details"] = capo_datazone.types.job_run_details.serialize_json(
            value["details"]
        )
    if "status" in value:
        import capo_datazone.types.job_run_status

        out["status"] = capo_datazone.types.job_run_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import capo_datazone.types.job_run_error

        out["error"] = capo_datazone.types.job_run_error.serialize_json(value["error"])
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["createdAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "start_time" in value:
        import capo_datazone.types._prelude.timestamp

        out["startTime"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_datazone.types._prelude.timestamp

        out["endTime"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> GetJobRunOutput:
    out: GetJobRunOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("jobType") is not None:
        import capo_datazone.types.job_type

        out["job_type"] = capo_datazone.types.job_type.deserialize_json(data["jobType"])
    if data.get("runMode") is not None:
        import capo_datazone.types.job_run_mode

        out["run_mode"] = capo_datazone.types.job_run_mode.deserialize_json(
            data["runMode"]
        )
    if data.get("details") is not None:
        import capo_datazone.types.job_run_details

        out["details"] = capo_datazone.types.job_run_details.deserialize_json(
            data["details"]
        )
    if data.get("status") is not None:
        import capo_datazone.types.job_run_status

        out["status"] = capo_datazone.types.job_run_status.deserialize_json(
            data["status"]
        )
    if data.get("error") is not None:
        import capo_datazone.types.job_run_error

        out["error"] = capo_datazone.types.job_run_error.deserialize_json(data["error"])
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("createdAt") is not None:
        import capo_datazone.types._prelude.timestamp

        out["created_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("startTime") is not None:
        import capo_datazone.types._prelude.timestamp

        out["start_time"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_datazone.types._prelude.timestamp

        out["end_time"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    return out

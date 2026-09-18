"""Generated from Smithy shape ``com.amazonaws.panorama#PackageImportJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.created_time
    import capo_panorama.types.job_id
    import capo_panorama.types.last_updated_time
    import capo_panorama.types.package_import_job_status
    import capo_panorama.types.package_import_job_status_message
    import capo_panorama.types.package_import_job_type


class PackageImportJob(TypedDict, closed=True):
    job_id: NotRequired["capo_panorama.types.job_id.JobId"]
    """<p>The job's ID.</p>"""
    job_type: NotRequired[
        "capo_panorama.types.package_import_job_type.PackageImportJobType"
    ]
    """<p>The job's type.</p>"""
    status: NotRequired[
        "capo_panorama.types.package_import_job_status.PackageImportJobStatus"
    ]
    """<p>The job's status.</p>"""
    status_message: NotRequired[
        "capo_panorama.types.package_import_job_status_message.PackageImportJobStatusMessage"
    ]
    """<p>The job's status message.</p>"""
    created_time: NotRequired["capo_panorama.types.created_time.CreatedTime"]
    """<p>When the job was created.</p>"""
    last_updated_time: NotRequired[
        "capo_panorama.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>When the job was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageImportJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_type" in value:
        out["JobType"] = value["job_type"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "created_time" in value:
        import capo_panorama.types.created_time

        out["CreatedTime"] = capo_panorama.types.created_time.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_panorama.types.last_updated_time

        out["LastUpdatedTime"] = capo_panorama.types.last_updated_time.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> PackageImportJob:
    out: PackageImportJob = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobType") is not None:
        out["job_type"] = data["JobType"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("CreatedTime") is not None:
        import capo_panorama.types.created_time

        out["created_time"] = capo_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_panorama.types.last_updated_time

        out["last_updated_time"] = (
            capo_panorama.types.last_updated_time.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out

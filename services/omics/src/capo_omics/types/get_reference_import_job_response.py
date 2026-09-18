"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.import_job_id
    import capo_omics.types.import_reference_source_list
    import capo_omics.types.job_status_message
    import capo_omics.types.reference_import_job_status
    import capo_omics.types.reference_store_id
    import capo_omics.types.role_arn


class GetReferenceImportJobResponse(TypedDict, closed=True):
    id: "capo_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The job's reference store ID.</p>"""
    role_arn: "capo_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "capo_omics.types.reference_import_job_status.ReferenceImportJobStatus"
    """<p>The job's status.</p>"""
    status_message: NotRequired["capo_omics.types.job_status_message.JobStatusMessage"]
    """<p>The job's status message.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""
    sources: "capo_omics.types.import_reference_source_list.ImportReferenceSourceList"
    """<p>The job's source files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReferenceImportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["roleArn"] = value["role_arn"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    if "completion_time" in value:
        import capo_omics._protocol.serialize

        out["completionTime"] = capo_omics._protocol.serialize.fmt_date_time(
            value["completion_time"]
        )
    import capo_omics.types.import_reference_source_list

    out["sources"] = capo_omics.types.import_reference_source_list.serialize_json(
        value["sources"]
    )
    return out


def deserialize_json(data: dict) -> GetReferenceImportJobResponse:
    out: GetReferenceImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetReferenceImportJobResponse.id required")
    if data.get("referenceStoreId") is not None:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        raise DeserializationError(
            "GetReferenceImportJobResponse.reference_store_id required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetReferenceImportJobResponse.role_arn required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetReferenceImportJobResponse.status required")
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "GetReferenceImportJobResponse.creation_time required"
        )
    if data.get("completionTime") is not None:
        import datetime

        out["completion_time"] = datetime.datetime.fromisoformat(
            data["completionTime"].replace("Z", "+00:00")
        )
    if data.get("sources") is not None:
        import capo_omics.types.import_reference_source_list

        out["sources"] = capo_omics.types.import_reference_source_list.deserialize_json(
            data["sources"]
        )
    else:
        raise DeserializationError("GetReferenceImportJobResponse.sources required")
    return out

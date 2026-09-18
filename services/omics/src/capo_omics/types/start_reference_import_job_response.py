"""Generated from Smithy shape ``com.amazonaws.omics#StartReferenceImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.import_job_id
    import capo_omics.types.reference_import_job_status
    import capo_omics.types.reference_store_id
    import capo_omics.types.role_arn


class StartReferenceImportJobResponse(TypedDict, closed=True):
    id: "capo_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The job's reference store ID.</p>"""
    role_arn: "capo_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "capo_omics.types.reference_import_job_status.ReferenceImportJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReferenceImportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["roleArn"] = value["role_arn"]
    out["status"] = value["status"]
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> StartReferenceImportJobResponse:
    out: StartReferenceImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartReferenceImportJobResponse.id required")
    if data.get("referenceStoreId") is not None:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        raise DeserializationError(
            "StartReferenceImportJobResponse.reference_store_id required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("StartReferenceImportJobResponse.role_arn required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("StartReferenceImportJobResponse.status required")
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "StartReferenceImportJobResponse.creation_time required"
        )
    return out

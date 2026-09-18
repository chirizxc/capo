"""Generated from Smithy shape ``com.amazonaws.omics#ImportReadSetJobItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.import_job_id
    import capo_omics.types.read_set_import_job_status
    import capo_omics.types.role_arn
    import capo_omics.types.sequence_store_id


class ImportReadSetJobItem(TypedDict, closed=True):
    id: "capo_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    role_arn: "capo_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "capo_omics.types.read_set_import_job_status.ReadSetImportJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportReadSetJobItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["roleArn"] = value["role_arn"]
    out["status"] = value["status"]
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    if "completion_time" in value:
        import capo_omics._protocol.serialize

        out["completionTime"] = capo_omics._protocol.serialize.fmt_date_time(
            value["completion_time"]
        )
    return out


def deserialize_json(data: dict) -> ImportReadSetJobItem:
    out: ImportReadSetJobItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ImportReadSetJobItem.id required")
    if data.get("sequenceStoreId") is not None:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError("ImportReadSetJobItem.sequence_store_id required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ImportReadSetJobItem.role_arn required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportReadSetJobItem.status required")
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("ImportReadSetJobItem.creation_time required")
    if data.get("completionTime") is not None:
        import datetime

        out["completion_time"] = datetime.datetime.fromisoformat(
            data["completionTime"].replace("Z", "+00:00")
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.export_job_id
    import capo_omics.types.export_read_set_detail_list
    import capo_omics.types.job_status_message
    import capo_omics.types.read_set_export_job_status
    import capo_omics.types.s3_destination
    import capo_omics.types.sequence_store_id


class GetReadSetExportJobResponse(TypedDict, closed=True):
    id: "capo_omics.types.export_job_id.ExportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    destination: "capo_omics.types.s3_destination.S3Destination"
    """<p>The job's destination in Amazon S3.</p>"""
    status: "capo_omics.types.read_set_export_job_status.ReadSetExportJobStatus"
    """<p>The job's status.</p>"""
    status_message: NotRequired["capo_omics.types.job_status_message.JobStatusMessage"]
    """<p>The job's status message.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""
    read_sets: NotRequired[
        "capo_omics.types.export_read_set_detail_list.ExportReadSetDetailList"
    ]
    """<p>The job's read sets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetExportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["destination"] = value["destination"]
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
    if "read_sets" in value:
        import capo_omics.types.export_read_set_detail_list

        out["readSets"] = capo_omics.types.export_read_set_detail_list.serialize_json(
            value["read_sets"]
        )
    return out


def deserialize_json(data: dict) -> GetReadSetExportJobResponse:
    out: GetReadSetExportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetReadSetExportJobResponse.id required")
    if data.get("sequenceStoreId") is not None:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "GetReadSetExportJobResponse.sequence_store_id required"
        )
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("GetReadSetExportJobResponse.destination required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetReadSetExportJobResponse.status required")
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("GetReadSetExportJobResponse.creation_time required")
    if data.get("completionTime") is not None:
        import datetime

        out["completion_time"] = datetime.datetime.fromisoformat(
            data["completionTime"].replace("Z", "+00:00")
        )
    if data.get("readSets") is not None:
        import capo_omics.types.export_read_set_detail_list

        out["read_sets"] = (
            capo_omics.types.export_read_set_detail_list.deserialize_json(
                data["readSets"]
            )
        )
    return out

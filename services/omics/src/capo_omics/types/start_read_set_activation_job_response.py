"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetActivationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.activation_job_id
    import capo_omics.types.read_set_activation_job_status
    import capo_omics.types.sequence_store_id


class StartReadSetActivationJobResponse(TypedDict, closed=True):
    id: "capo_omics.types.activation_job_id.ActivationJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    status: "capo_omics.types.read_set_activation_job_status.ReadSetActivationJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetActivationJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["status"] = value["status"]
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> StartReadSetActivationJobResponse:
    out: StartReadSetActivationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartReadSetActivationJobResponse.id required")
    if data.get("sequenceStoreId") is not None:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "StartReadSetActivationJobResponse.sequence_store_id required"
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("StartReadSetActivationJobResponse.status required")
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "StartReadSetActivationJobResponse.creation_time required"
        )
    return out

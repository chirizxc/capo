"""Generated from Smithy shape ``com.amazonaws.healthlake#StartDataTransformationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_job_id
    import capo_healthlake.types.transformation_job_status


class StartDataTransformationJobResponse(TypedDict, closed=True):
    job_id: "capo_healthlake.types.data_transformation_job_id.DataTransformationJobId"
    """<p>The unique identifier assigned to the data transformation job.</p>"""
    job_status: (
        "capo_healthlake.types.transformation_job_status.TransformationJobStatus"
    )
    """<p>The initial status of the data transformation job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDataTransformationJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    import capo_healthlake.types.transformation_job_status

    out["JobStatus"] = (
        capo_healthlake.types.transformation_job_status.serialize_aws_json_1_0(
            value["job_status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDataTransformationJobResponse:
    out: StartDataTransformationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StartDataTransformationJobResponse.job_id required")
    if data.get("JobStatus") is not None:
        import capo_healthlake.types.transformation_job_status

        out["job_status"] = (
            capo_healthlake.types.transformation_job_status.deserialize_aws_json_1_0(
                data["JobStatus"]
            )
        )
    else:
        raise DeserializationError(
            "StartDataTransformationJobResponse.job_status required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.healthlake#DescribeDataTransformationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.transformation_job_properties


class DescribeDataTransformationJobResponse(TypedDict, closed=True):
    transformation_job_properties: "capo_healthlake.types.transformation_job_properties.TransformationJobProperties"
    """<p>The properties of the data transformation job, including status, configuration, and progress information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDataTransformationJobResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.transformation_job_properties

    out["TransformationJobProperties"] = (
        capo_healthlake.types.transformation_job_properties.serialize_aws_json_1_0(
            value["transformation_job_properties"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDataTransformationJobResponse:
    out: DescribeDataTransformationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TransformationJobProperties") is not None:
        import capo_healthlake.types.transformation_job_properties

        out["transformation_job_properties"] = (
            capo_healthlake.types.transformation_job_properties.deserialize_aws_json_1_0(
                data["TransformationJobProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDataTransformationJobResponse.transformation_job_properties required"
        )
    return out

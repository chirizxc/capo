"""Generated from Smithy shape ``com.amazonaws.healthlake#TransformationOutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_s3_configuration


class TransformationOutputDataConfig(TypedDict, closed=True):
    s3_configuration: "capo_healthlake.types.data_transformation_s3_configuration.DataTransformationS3Configuration"
    """<p>The Amazon S3 output location and Amazon Web Services Key Management Service (Amazon Web Services KMS) encryption configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformationOutputDataConfig) -> dict:
    out: dict = {}
    import capo_healthlake.types.data_transformation_s3_configuration

    out["S3Configuration"] = (
        capo_healthlake.types.data_transformation_s3_configuration.serialize_aws_json_1_0(
            value["s3_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransformationOutputDataConfig:
    out: TransformationOutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Configuration") is not None:
        import capo_healthlake.types.data_transformation_s3_configuration

        out["s3_configuration"] = (
            capo_healthlake.types.data_transformation_s3_configuration.deserialize_aws_json_1_0(
                data["S3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "TransformationOutputDataConfig.s3_configuration required"
        )
    return out

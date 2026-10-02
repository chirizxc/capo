"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#Code``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mwaa_serverless.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.s3_location


class _Code_S3Location(TypedDict, closed=True):
    S3Location: "capo_mwaa_serverless.types.s3_location.S3Location"


Code: TypeAlias = _Code_S3Location


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Code) -> dict:
    if "S3Location" in value:
        import capo_mwaa_serverless.types.s3_location

        return {
            "S3Location": capo_mwaa_serverless.types.s3_location.serialize_aws_json_1_0(
                value["S3Location"]
            )
        }
    else:
        raise SerializationError("Code: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Code:
    if data.get("S3Location") is not None:
        import capo_mwaa_serverless.types.s3_location

        return {
            "S3Location": capo_mwaa_serverless.types.s3_location.deserialize_aws_json_1_0(
                data["S3Location"]
            )
        }
    else:
        raise DeserializationError("Code: no recognized variant key")

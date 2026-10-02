"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetSpaceCredentialsForOrganizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.aws_credentials


class GetSpaceCredentialsForOrganizationOutput(TypedDict, closed=True):
    credentials: "capo_cloudwatchomni.types.aws_credentials.AwsCredentials"
    """The temporary AWS credentials for the space."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSpaceCredentialsForOrganizationOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.aws_credentials

    out["credentials"] = capo_cloudwatchomni.types.aws_credentials.serialize_cbor(
        value["credentials"]
    )
    return out


def deserialize_cbor(data: dict) -> GetSpaceCredentialsForOrganizationOutput:
    out: GetSpaceCredentialsForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("credentials") is not None:
        import capo_cloudwatchomni.types.aws_credentials

        out["credentials"] = capo_cloudwatchomni.types.aws_credentials.deserialize_cbor(
            data["credentials"]
        )
    else:
        raise DeserializationError(
            "GetSpaceCredentialsForOrganizationOutput.credentials required"
        )
    return out

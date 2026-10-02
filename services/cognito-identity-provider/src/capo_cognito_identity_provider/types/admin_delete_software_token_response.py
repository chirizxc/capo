"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminDeleteSoftwareTokenResponse``."""

from typing_extensions import TypedDict


class AdminDeleteSoftwareTokenResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminDeleteSoftwareTokenResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminDeleteSoftwareTokenResponse:
    out: AdminDeleteSoftwareTokenResponse = {}  # type: ignore[typeddict-item]
    return out

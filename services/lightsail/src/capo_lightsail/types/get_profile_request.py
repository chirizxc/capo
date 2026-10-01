"""Generated from Smithy shape ``com.amazonaws.lightsail#GetProfileRequest``."""

from typing_extensions import TypedDict


class GetProfileRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProfileRequest:
    out: GetProfileRequest = {}  # type: ignore[typeddict-item]
    return out

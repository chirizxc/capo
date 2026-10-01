"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetStorageTierPolicyRequest``."""

from typing_extensions import TypedDict


class GetStorageTierPolicyRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStorageTierPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStorageTierPolicyRequest:
    out: GetStorageTierPolicyRequest = {}  # type: ignore[typeddict-item]
    return out

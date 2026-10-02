"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetStorageTierPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.storage_tier
    import capo_cloudwatch_logs.types.timestamp


class GetStorageTierPolicyResponse(TypedDict, closed=True):
    storage_tier: NotRequired["capo_cloudwatch_logs.types.storage_tier.StorageTier"]
    """<p>The current storage tier for the account.</p>"""
    last_updated_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time when the storage tier policy was last updated, expressed as the number of milliseconds after <code>January 1, 1970 00:00:00 UTC</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStorageTierPolicyResponse) -> dict:
    out: dict = {}
    if "storage_tier" in value:
        import capo_cloudwatch_logs.types.storage_tier

        out["storageTier"] = (
            capo_cloudwatch_logs.types.storage_tier.serialize_aws_json_1_1(
                value["storage_tier"]
            )
        )
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStorageTierPolicyResponse:
    out: GetStorageTierPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("storageTier") is not None:
        import capo_cloudwatch_logs.types.storage_tier

        out["storage_tier"] = (
            capo_cloudwatch_logs.types.storage_tier.deserialize_aws_json_1_1(
                data["storageTier"]
            )
        )
    if data.get("lastUpdatedTime") is not None:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out

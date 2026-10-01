"""Generated from Smithy shape ``com.amazonaws.odb#ExascaleDbStorageDetails``."""

from typing_extensions import NotRequired, TypedDict


class ExascaleDbStorageDetails(TypedDict, closed=True):
    available_size_in_g_bs: NotRequired["int"]
    """<p>The available storage size, in gigabytes (GB).</p>"""
    total_size_in_g_bs: NotRequired["int"]
    """<p>The total storage size, in gigabytes (GB).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExascaleDbStorageDetails) -> dict:
    out: dict = {}
    if "available_size_in_g_bs" in value:
        out["availableSizeInGBs"] = value["available_size_in_g_bs"]
    if "total_size_in_g_bs" in value:
        out["totalSizeInGBs"] = value["total_size_in_g_bs"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExascaleDbStorageDetails:
    out: ExascaleDbStorageDetails = {}  # type: ignore[typeddict-item]
    if data.get("availableSizeInGBs") is not None:
        out["available_size_in_g_bs"] = data["availableSizeInGBs"]
    if data.get("totalSizeInGBs") is not None:
        out["total_size_in_g_bs"] = data["totalSizeInGBs"]
    return out

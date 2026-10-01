"""Generated from Smithy shape ``com.amazonaws.odb#ExadbVmClusterStorageDetails``."""

from typing_extensions import NotRequired, TypedDict


class ExadbVmClusterStorageDetails(TypedDict, closed=True):
    total_size_in_g_bs: NotRequired["int"]
    """<p>The total storage size, in gigabytes (GB).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExadbVmClusterStorageDetails) -> dict:
    out: dict = {}
    if "total_size_in_g_bs" in value:
        out["totalSizeInGBs"] = value["total_size_in_g_bs"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExadbVmClusterStorageDetails:
    out: ExadbVmClusterStorageDetails = {}  # type: ignore[typeddict-item]
    if data.get("totalSizeInGBs") is not None:
        out["total_size_in_g_bs"] = data["totalSizeInGBs"]
    return out

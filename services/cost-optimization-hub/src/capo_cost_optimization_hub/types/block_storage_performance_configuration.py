"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#BlockStoragePerformanceConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class BlockStoragePerformanceConfiguration(TypedDict, closed=True):
    iops: NotRequired["float"]
    """<p>The number of I/O operations per second.</p>"""
    throughput: NotRequired["float"]
    """<p>The throughput that the volume supports.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlockStoragePerformanceConfiguration) -> dict:
    out: dict = {}
    if "iops" in value:
        out["iops"] = (
            "NaN"
            if value["iops"] != value["iops"]
            else "Infinity"
            if value["iops"] == float("inf")
            else "-Infinity"
            if value["iops"] == float("-inf")
            else value["iops"]
        )
    if "throughput" in value:
        out["throughput"] = (
            "NaN"
            if value["throughput"] != value["throughput"]
            else "Infinity"
            if value["throughput"] == float("inf")
            else "-Infinity"
            if value["throughput"] == float("-inf")
            else value["throughput"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BlockStoragePerformanceConfiguration:
    out: BlockStoragePerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("iops") is not None:
        out["iops"] = float(data["iops"])
    if data.get("throughput") is not None:
        out["throughput"] = float(data["throughput"])
    return out

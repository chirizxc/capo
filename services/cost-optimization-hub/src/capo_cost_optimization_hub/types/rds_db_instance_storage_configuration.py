"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RdsDbInstanceStorageConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class RdsDbInstanceStorageConfiguration(TypedDict, closed=True):
    storage_type: NotRequired["str"]
    """<p>The storage type to associate with the DB instance.</p>"""
    allocated_storage_in_gb: NotRequired["float"]
    """<p>The new amount of storage in GB to allocate for the DB instance.</p>"""
    iops: NotRequired["float"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.</p>"""
    storage_throughput: NotRequired["float"]
    """<p>The storage throughput for the DB instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsDbInstanceStorageConfiguration) -> dict:
    out: dict = {}
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "allocated_storage_in_gb" in value:
        out["allocatedStorageInGb"] = (
            "NaN"
            if value["allocated_storage_in_gb"] != value["allocated_storage_in_gb"]
            else "Infinity"
            if value["allocated_storage_in_gb"] == float("inf")
            else "-Infinity"
            if value["allocated_storage_in_gb"] == float("-inf")
            else value["allocated_storage_in_gb"]
        )
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
    if "storage_throughput" in value:
        out["storageThroughput"] = (
            "NaN"
            if value["storage_throughput"] != value["storage_throughput"]
            else "Infinity"
            if value["storage_throughput"] == float("inf")
            else "-Infinity"
            if value["storage_throughput"] == float("-inf")
            else value["storage_throughput"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RdsDbInstanceStorageConfiguration:
    out: RdsDbInstanceStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("allocatedStorageInGb") is not None:
        out["allocated_storage_in_gb"] = float(data["allocatedStorageInGb"])
    if data.get("iops") is not None:
        out["iops"] = float(data["iops"])
    if data.get("storageThroughput") is not None:
        out["storage_throughput"] = float(data["storageThroughput"])
    return out

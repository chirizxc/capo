"""Generated from Smithy shape ``com.amazonaws.emrserverless#TotalResourceUtilization``."""

from typing_extensions import NotRequired, TypedDict


class TotalResourceUtilization(TypedDict, closed=True):
    v_cpu_hour: NotRequired["float"]
    """<p>The aggregated vCPU used per hour from the time job start executing till the time job is terminated.</p>"""
    memory_gb_hour: NotRequired["float"]
    """<p>The aggregated memory used per hour from the time job start executing till the time job is terminated.</p>"""
    storage_gb_hour: NotRequired["float"]
    """<p>The aggregated storage used per hour from the time job start executing till the time job is terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TotalResourceUtilization) -> dict:
    out: dict = {}
    if "v_cpu_hour" in value:
        out["vCPUHour"] = (
            "NaN"
            if value["v_cpu_hour"] != value["v_cpu_hour"]
            else "Infinity"
            if value["v_cpu_hour"] == float("inf")
            else "-Infinity"
            if value["v_cpu_hour"] == float("-inf")
            else value["v_cpu_hour"]
        )
    if "memory_gb_hour" in value:
        out["memoryGBHour"] = (
            "NaN"
            if value["memory_gb_hour"] != value["memory_gb_hour"]
            else "Infinity"
            if value["memory_gb_hour"] == float("inf")
            else "-Infinity"
            if value["memory_gb_hour"] == float("-inf")
            else value["memory_gb_hour"]
        )
    if "storage_gb_hour" in value:
        out["storageGBHour"] = (
            "NaN"
            if value["storage_gb_hour"] != value["storage_gb_hour"]
            else "Infinity"
            if value["storage_gb_hour"] == float("inf")
            else "-Infinity"
            if value["storage_gb_hour"] == float("-inf")
            else value["storage_gb_hour"]
        )
    return out


def deserialize_json(data: dict) -> TotalResourceUtilization:
    out: TotalResourceUtilization = {}  # type: ignore[typeddict-item]
    if data.get("vCPUHour") is not None:
        out["v_cpu_hour"] = float(data["vCPUHour"])
    if data.get("memoryGBHour") is not None:
        out["memory_gb_hour"] = float(data["memoryGBHour"])
    if data.get("storageGBHour") is not None:
        out["storage_gb_hour"] = float(data["storageGBHour"])
    return out

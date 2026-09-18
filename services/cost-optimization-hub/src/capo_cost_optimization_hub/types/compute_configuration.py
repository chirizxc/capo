"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ComputeConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class ComputeConfiguration(TypedDict, closed=True):
    v_cpu: NotRequired["float"]
    """<p>The number of vCPU cores in the resource.</p>"""
    memory_size_in_mb: NotRequired["int"]
    """<p>The memory size of the resource.</p>"""
    architecture: NotRequired["str"]
    """<p>The architecture of the resource.</p>"""
    platform: NotRequired["str"]
    """<p>The platform of the resource. The platform is the specific combination of operating system, license model, and software on an instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeConfiguration) -> dict:
    out: dict = {}
    if "v_cpu" in value:
        out["vCpu"] = (
            "NaN"
            if value["v_cpu"] != value["v_cpu"]
            else "Infinity"
            if value["v_cpu"] == float("inf")
            else "-Infinity"
            if value["v_cpu"] == float("-inf")
            else value["v_cpu"]
        )
    if "memory_size_in_mb" in value:
        out["memorySizeInMB"] = value["memory_size_in_mb"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ComputeConfiguration:
    out: ComputeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("vCpu") is not None:
        out["v_cpu"] = float(data["vCpu"])
    if data.get("memorySizeInMB") is not None:
        out["memory_size_in_mb"] = data["memorySizeInMB"]
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    return out

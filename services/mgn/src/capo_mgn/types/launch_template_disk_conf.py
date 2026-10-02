"""Generated from Smithy shape ``com.amazonaws.mgn#LaunchTemplateDiskConf``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.iops
    import capo_mgn.types.throughput
    import capo_mgn.types.volume_initialization_rate
    import capo_mgn.types.volume_type


class LaunchTemplateDiskConf(TypedDict, closed=True):
    volume_type: NotRequired["capo_mgn.types.volume_type.VolumeType"]
    """<p>Launch template disk volume type configuration.</p>"""
    iops: NotRequired["capo_mgn.types.iops.Iops"]
    """<p>Launch template disk iops configuration.</p>"""
    throughput: NotRequired["capo_mgn.types.throughput.Throughput"]
    """<p>Launch template disk throughput configuration.</p>"""
    volume_initialization_rate: NotRequired[
        "capo_mgn.types.volume_initialization_rate.VolumeInitializationRate"
    ]
    """<p>Launch template disk volume initialization rate configuration.</p>"""
    delete_on_termination: NotRequired["bool"]
    """<p>Launch template disk delete on termination configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateDiskConf) -> dict:
    out: dict = {}
    if "volume_type" in value:
        out["volumeType"] = value["volume_type"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    if "volume_initialization_rate" in value:
        out["volumeInitializationRate"] = value["volume_initialization_rate"]
    if "delete_on_termination" in value:
        out["deleteOnTermination"] = value["delete_on_termination"]
    return out


def deserialize_json(data: dict) -> LaunchTemplateDiskConf:
    out: LaunchTemplateDiskConf = {}  # type: ignore[typeddict-item]
    if data.get("volumeType") is not None:
        out["volume_type"] = data["volumeType"]
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("throughput") is not None:
        out["throughput"] = data["throughput"]
    if data.get("volumeInitializationRate") is not None:
        out["volume_initialization_rate"] = data["volumeInitializationRate"]
    if data.get("deleteOnTermination") is not None:
        out["delete_on_termination"] = data["deleteOnTermination"]
    return out

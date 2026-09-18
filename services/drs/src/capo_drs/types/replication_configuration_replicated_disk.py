"""Generated from Smithy shape ``com.amazonaws.drs#ReplicationConfigurationReplicatedDisk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.bounded_string
    import capo_drs.types.positive_integer
    import capo_drs.types.replication_configuration_replicated_disk_staging_disk_type


class ReplicationConfigurationReplicatedDisk(TypedDict, closed=True):
    device_name: NotRequired["capo_drs.types.bounded_string.BoundedString"]
    """<p>The name of the device.</p>"""
    is_boot_disk: NotRequired["bool"]
    """<p>Whether to boot from this disk or not.</p>"""
    staging_disk_type: NotRequired[
        "capo_drs.types.replication_configuration_replicated_disk_staging_disk_type.ReplicationConfigurationReplicatedDiskStagingDiskType"
    ]
    """<p>The Staging Disk EBS volume type to be used during replication.</p>"""
    iops: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The requested number of I/O operations per second (IOPS).</p>"""
    throughput: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The throughput to use for the EBS volume in MiB/s. This parameter is valid only for gp3 volumes.</p>"""
    optimized_staging_disk_type: NotRequired[
        "capo_drs.types.replication_configuration_replicated_disk_staging_disk_type.ReplicationConfigurationReplicatedDiskStagingDiskType"
    ]
    """<p>The Staging Disk EBS volume type to be used during replication when <code>stagingDiskType</code> is set to Auto. This is a read-only field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationReplicatedDisk) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    if "is_boot_disk" in value:
        out["isBootDisk"] = value["is_boot_disk"]
    if "staging_disk_type" in value:
        out["stagingDiskType"] = value["staging_disk_type"]
    out["iops"] = value.get("iops", 0)
    out["throughput"] = value.get("throughput", 0)
    if "optimized_staging_disk_type" in value:
        out["optimizedStagingDiskType"] = value["optimized_staging_disk_type"]
    return out


def deserialize_json(data: dict) -> ReplicationConfigurationReplicatedDisk:
    out: ReplicationConfigurationReplicatedDisk = {}  # type: ignore[typeddict-item]
    if data.get("deviceName") is not None:
        out["device_name"] = data["deviceName"]
    if data.get("isBootDisk") is not None:
        out["is_boot_disk"] = data["isBootDisk"]
    if data.get("stagingDiskType") is not None:
        out["staging_disk_type"] = data["stagingDiskType"]
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    else:
        out["iops"] = 0
    if data.get("throughput") is not None:
        out["throughput"] = data["throughput"]
    else:
        out["throughput"] = 0
    if data.get("optimizedStagingDiskType") is not None:
        out["optimized_staging_disk_type"] = data["optimizedStagingDiskType"]
    return out

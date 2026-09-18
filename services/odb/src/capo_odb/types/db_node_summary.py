"""Generated from Smithy shape ``com.amazonaws.odb#DbNodeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.db_node_maintenance_type
    import capo_odb.types.db_node_resource_status
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_id


class DbNodeSummary(TypedDict, closed=True):
    db_node_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the DB node.</p>"""
    db_node_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the DB node.</p>"""
    status: NotRequired["capo_odb.types.db_node_resource_status.DbNodeResourceStatus"]
    """<p>The current status of the DB node.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the DB node.</p>"""
    additional_details: NotRequired["str"]
    """<p>Additional information about the planned maintenance.</p>"""
    backup_ip_id: NotRequired["str"]
    """<p>The Oracle Cloud ID (OCID) of the backup IP address that's associated with the DB node.</p>"""
    backup_vnic2_id: NotRequired["str"]
    """<p>The OCID of the second backup virtual network interface card (VNIC) for the DB node.</p>"""
    backup_vnic_id: NotRequired["str"]
    """<p>The OCID of the backup VNIC for the DB node.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores enabled on the DB node.</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of local node storage, in gigabytes (GB), that's allocated on the DB node.</p>"""
    db_server_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the database server that's associated with the DB node.</p>"""
    db_system_id: NotRequired["str"]
    """<p>The OCID of the DB system.</p>"""
    fault_domain: NotRequired["str"]
    """<p>The name of the fault domain where the DB node is located.</p>"""
    host_ip_id: NotRequired["str"]
    """<p>The OCID of the host IP address that's associated with the DB node.</p>"""
    hostname: NotRequired["str"]
    """<p>The host name for the DB node.</p>"""
    ocid: NotRequired["str"]
    """<p>The OCID of the DB node.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor for the DB node.</p>"""
    maintenance_type: NotRequired[
        "capo_odb.types.db_node_maintenance_type.DbNodeMaintenanceType"
    ]
    """<p>The type of maintenance the DB node. </p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory, in gigabytes (GB), that allocated on the DB node.</p>"""
    software_storage_size_in_gb: NotRequired["int"]
    """<p>The size of the block storage volume, in gigabytes (GB), that's allocated for the DB system. This attribute applies only for virtual machine DB systems.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the DB node was created.</p>"""
    time_maintenance_window_end: NotRequired["str"]
    """<p>The end date and time of the maintenance window.</p>"""
    time_maintenance_window_start: NotRequired["str"]
    """<p>The start date and time of the maintenance window.</p>"""
    total_cpu_core_count: NotRequired["int"]
    """<p>The total number of CPU cores reserved on the DB node.</p>"""
    vnic2_id: NotRequired["str"]
    """<p>The OCID of the second VNIC.</p>"""
    vnic_id: NotRequired["str"]
    """<p>The OCID of the VNIC.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbNodeSummary) -> dict:
    out: dict = {}
    if "db_node_id" in value:
        out["dbNodeId"] = value["db_node_id"]
    if "db_node_arn" in value:
        out["dbNodeArn"] = value["db_node_arn"]
    if "status" in value:
        import capo_odb.types.db_node_resource_status

        out["status"] = capo_odb.types.db_node_resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "additional_details" in value:
        out["additionalDetails"] = value["additional_details"]
    if "backup_ip_id" in value:
        out["backupIpId"] = value["backup_ip_id"]
    if "backup_vnic2_id" in value:
        out["backupVnic2Id"] = value["backup_vnic2_id"]
    if "backup_vnic_id" in value:
        out["backupVnicId"] = value["backup_vnic_id"]
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "db_server_id" in value:
        out["dbServerId"] = value["db_server_id"]
    if "db_system_id" in value:
        out["dbSystemId"] = value["db_system_id"]
    if "fault_domain" in value:
        out["faultDomain"] = value["fault_domain"]
    if "host_ip_id" in value:
        out["hostIpId"] = value["host_ip_id"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "maintenance_type" in value:
        import capo_odb.types.db_node_maintenance_type

        out["maintenanceType"] = (
            capo_odb.types.db_node_maintenance_type.serialize_aws_json_1_0(
                value["maintenance_type"]
            )
        )
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "software_storage_size_in_gb" in value:
        out["softwareStorageSizeInGB"] = value["software_storage_size_in_gb"]
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "time_maintenance_window_end" in value:
        out["timeMaintenanceWindowEnd"] = value["time_maintenance_window_end"]
    if "time_maintenance_window_start" in value:
        out["timeMaintenanceWindowStart"] = value["time_maintenance_window_start"]
    if "total_cpu_core_count" in value:
        out["totalCpuCoreCount"] = value["total_cpu_core_count"]
    if "vnic2_id" in value:
        out["vnic2Id"] = value["vnic2_id"]
    if "vnic_id" in value:
        out["vnicId"] = value["vnic_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbNodeSummary:
    out: DbNodeSummary = {}  # type: ignore[typeddict-item]
    if data.get("dbNodeId") is not None:
        out["db_node_id"] = data["dbNodeId"]
    if data.get("dbNodeArn") is not None:
        out["db_node_arn"] = data["dbNodeArn"]
    if data.get("status") is not None:
        import capo_odb.types.db_node_resource_status

        out["status"] = capo_odb.types.db_node_resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("additionalDetails") is not None:
        out["additional_details"] = data["additionalDetails"]
    if data.get("backupIpId") is not None:
        out["backup_ip_id"] = data["backupIpId"]
    if data.get("backupVnic2Id") is not None:
        out["backup_vnic2_id"] = data["backupVnic2Id"]
    if data.get("backupVnicId") is not None:
        out["backup_vnic_id"] = data["backupVnicId"]
    if data.get("cpuCoreCount") is not None:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if data.get("dbNodeStorageSizeInGBs") is not None:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if data.get("dbServerId") is not None:
        out["db_server_id"] = data["dbServerId"]
    if data.get("dbSystemId") is not None:
        out["db_system_id"] = data["dbSystemId"]
    if data.get("faultDomain") is not None:
        out["fault_domain"] = data["faultDomain"]
    if data.get("hostIpId") is not None:
        out["host_ip_id"] = data["hostIpId"]
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    if data.get("ocid") is not None:
        out["ocid"] = data["ocid"]
    if data.get("ociResourceAnchorName") is not None:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if data.get("maintenanceType") is not None:
        import capo_odb.types.db_node_maintenance_type

        out["maintenance_type"] = (
            capo_odb.types.db_node_maintenance_type.deserialize_aws_json_1_0(
                data["maintenanceType"]
            )
        )
    if data.get("memorySizeInGBs") is not None:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if data.get("softwareStorageSizeInGB") is not None:
        out["software_storage_size_in_gb"] = data["softwareStorageSizeInGB"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("timeMaintenanceWindowEnd") is not None:
        out["time_maintenance_window_end"] = data["timeMaintenanceWindowEnd"]
    if data.get("timeMaintenanceWindowStart") is not None:
        out["time_maintenance_window_start"] = data["timeMaintenanceWindowStart"]
    if data.get("totalCpuCoreCount") is not None:
        out["total_cpu_core_count"] = data["totalCpuCoreCount"]
    if data.get("vnic2Id") is not None:
        out["vnic2_id"] = data["vnic2Id"]
    if data.get("vnicId") is not None:
        out["vnic_id"] = data["vnicId"]
    return out

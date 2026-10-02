"""Generated from Smithy shape ``com.amazonaws.odb#ExadbVmClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.exadb_vm_cluster_summary

ExadbVmClusterList: TypeAlias = list[
    "capo_odb.types.exadb_vm_cluster_summary.ExadbVmClusterSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExadbVmClusterList) -> list:
    import capo_odb.types.exadb_vm_cluster_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.exadb_vm_cluster_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ExadbVmClusterList:
    import capo_odb.types.exadb_vm_cluster_summary

    out: ExadbVmClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_odb.types.exadb_vm_cluster_summary.deserialize_aws_json_1_0(item)
        )
    return out

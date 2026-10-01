"""Generated from Smithy shape ``com.amazonaws.odb#GetExadbVmClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_odb.types.exadb_vm_cluster


class GetExadbVmClusterOutput(TypedDict, closed=True):
    exadb_vm_cluster: "capo_odb.types.exadb_vm_cluster.ExadbVmCluster"
    """<p>The Exascale VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetExadbVmClusterOutput) -> dict:
    out: dict = {}
    import capo_odb.types.exadb_vm_cluster

    out["exadbVmCluster"] = capo_odb.types.exadb_vm_cluster.serialize_aws_json_1_0(
        value["exadb_vm_cluster"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetExadbVmClusterOutput:
    out: GetExadbVmClusterOutput = {}  # type: ignore[typeddict-item]
    if data.get("exadbVmCluster") is not None:
        import capo_odb.types.exadb_vm_cluster

        out["exadb_vm_cluster"] = (
            capo_odb.types.exadb_vm_cluster.deserialize_aws_json_1_0(
                data["exadbVmCluster"]
            )
        )
    else:
        raise DeserializationError("GetExadbVmClusterOutput.exadb_vm_cluster required")
    return out

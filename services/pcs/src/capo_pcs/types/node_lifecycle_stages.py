"""Generated from Smithy shape ``com.amazonaws.pcs#NodeLifecycleStages``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.node_lifecycle_script_list


class NodeLifecycleStages(TypedDict, closed=True):
    node_bootstrapped: NotRequired[
        "capo_pcs.types.node_lifecycle_script_list.NodeLifecycleScriptList"
    ]
    """<p>The scripts to run after PCS finishes setting up the compute node and before the Slurm daemon (<code>slurmd</code>) starts. Use this stage for tasks that must complete before the node accepts jobs, such as mounting shared storage, configuring networking, or installing software packages.</p>"""
    node_ready: NotRequired[
        "capo_pcs.types.node_lifecycle_script_list.NodeLifecycleScriptList"
    ]
    """<p>The scripts to run after the Slurm daemon (<code>slurmd</code>) starts and the compute node registers with the Slurm controller. Use this stage for tasks that require Slurm to be running, such as running Slurm commands.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeLifecycleStages) -> dict:
    out: dict = {}
    if "node_bootstrapped" in value:
        import capo_pcs.types.node_lifecycle_script_list

        out["nodeBootstrapped"] = (
            capo_pcs.types.node_lifecycle_script_list.serialize_aws_json_1_0(
                value["node_bootstrapped"]
            )
        )
    if "node_ready" in value:
        import capo_pcs.types.node_lifecycle_script_list

        out["nodeReady"] = (
            capo_pcs.types.node_lifecycle_script_list.serialize_aws_json_1_0(
                value["node_ready"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NodeLifecycleStages:
    out: NodeLifecycleStages = {}  # type: ignore[typeddict-item]
    if data.get("nodeBootstrapped") is not None:
        import capo_pcs.types.node_lifecycle_script_list

        out["node_bootstrapped"] = (
            capo_pcs.types.node_lifecycle_script_list.deserialize_aws_json_1_0(
                data["nodeBootstrapped"]
            )
        )
    if data.get("nodeReady") is not None:
        import capo_pcs.types.node_lifecycle_script_list

        out["node_ready"] = (
            capo_pcs.types.node_lifecycle_script_list.deserialize_aws_json_1_0(
                data["nodeReady"]
            )
        )
    return out

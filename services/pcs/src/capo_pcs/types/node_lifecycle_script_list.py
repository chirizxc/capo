"""Generated from Smithy shape ``com.amazonaws.pcs#NodeLifecycleScriptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.node_lifecycle_script

NodeLifecycleScriptList: TypeAlias = list[
    "capo_pcs.types.node_lifecycle_script.NodeLifecycleScript"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeLifecycleScriptList) -> list:
    import capo_pcs.types.node_lifecycle_script

    out: list = []
    for item in value:
        out.append(capo_pcs.types.node_lifecycle_script.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> NodeLifecycleScriptList:
    import capo_pcs.types.node_lifecycle_script

    out: NodeLifecycleScriptList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pcs.types.node_lifecycle_script.deserialize_aws_json_1_0(item))
    return out

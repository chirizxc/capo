"""Generated from Smithy shape ``com.amazonaws.pcs#NodeLifecycleScriptArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.node_lifecycle_script_argument

NodeLifecycleScriptArguments: TypeAlias = list[
    "capo_pcs.types.node_lifecycle_script_argument.NodeLifecycleScriptArgument"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeLifecycleScriptArguments) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NodeLifecycleScriptArguments:
    return [item for item in data if item is not None]

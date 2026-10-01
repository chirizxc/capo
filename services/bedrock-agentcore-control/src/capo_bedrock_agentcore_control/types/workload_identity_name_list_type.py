"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WorkloadIdentityNameListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.workload_identity_name_type

WorkloadIdentityNameListType: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadIdentityNameListType) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadIdentityNameListType:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEndpointStatus``."""

from typing import Literal, TypeAlias, cast

HarnessEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> HarnessEndpointStatus:
    return cast(HarnessEndpointStatus, data)

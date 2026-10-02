"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentEventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_event_metadata_key
    import capo_launch_wizard.types.deployment_event_metadata_value

DeploymentEventMetadata: TypeAlias = dict[
    "capo_launch_wizard.types.deployment_event_metadata_key.DeploymentEventMetadataKey",
    "capo_launch_wizard.types.deployment_event_metadata_value.DeploymentEventMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DeploymentEventMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DeploymentEventMetadata:
    out: DeploymentEventMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out

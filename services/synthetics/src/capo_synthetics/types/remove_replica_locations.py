"""Generated from Smithy shape ``com.amazonaws.synthetics#RemoveReplicaLocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.location

RemoveReplicaLocations: TypeAlias = list["capo_synthetics.types.location.Location"]


# --- restJson1 ser/de ---
def serialize_json(value: RemoveReplicaLocations) -> list:
    return list(value)


def deserialize_json(data: list) -> RemoveReplicaLocations:
    return [item for item in data if item is not None]

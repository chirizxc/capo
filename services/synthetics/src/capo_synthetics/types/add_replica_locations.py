"""Generated from Smithy shape ``com.amazonaws.synthetics#AddReplicaLocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.add_replica_location_input

AddReplicaLocations: TypeAlias = list[
    "capo_synthetics.types.add_replica_location_input.AddReplicaLocationInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: AddReplicaLocations) -> list:
    import capo_synthetics.types.add_replica_location_input

    out: list = []
    for item in value:
        out.append(
            capo_synthetics.types.add_replica_location_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AddReplicaLocations:
    import capo_synthetics.types.add_replica_location_input

    out: AddReplicaLocations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_synthetics.types.add_replica_location_input.deserialize_json(item)
        )
    return out

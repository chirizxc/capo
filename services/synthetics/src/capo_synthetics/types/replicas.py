"""Generated from Smithy shape ``com.amazonaws.synthetics#Replicas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.replica

Replicas: TypeAlias = list["capo_synthetics.types.replica.Replica"]


# --- restJson1 ser/de ---
def serialize_json(value: Replicas) -> list:
    import capo_synthetics.types.replica

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.replica.serialize_json(item))
    return out


def deserialize_json(data: list) -> Replicas:
    import capo_synthetics.types.replica

    out: Replicas = []
    for item in data:
        if item is None:
            continue
        out.append(capo_synthetics.types.replica.deserialize_json(item))
    return out

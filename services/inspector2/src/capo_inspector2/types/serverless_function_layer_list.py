"""Generated from Smithy shape ``com.amazonaws.inspector2#ServerlessFunctionLayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.serverless_function_layer_urn

ServerlessFunctionLayerList: TypeAlias = list[
    "capo_inspector2.types.serverless_function_layer_urn.ServerlessFunctionLayerUrn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServerlessFunctionLayerList) -> list:
    return list(value)


def deserialize_json(data: list) -> ServerlessFunctionLayerList:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeExecutionDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_node_execution_details

ComputeNodeExecutionDetailsList: TypeAlias = list[
    "capo_iotsitewise.types.compute_node_execution_details.ComputeNodeExecutionDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNodeExecutionDetailsList) -> list:
    import capo_iotsitewise.types.compute_node_execution_details

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.compute_node_execution_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComputeNodeExecutionDetailsList:
    import capo_iotsitewise.types.compute_node_execution_details

    out: ComputeNodeExecutionDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.compute_node_execution_details.deserialize_json(item)
        )
    return out

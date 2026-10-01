"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionEnvironmentVariables``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_node_environment_variables_map
    import capo_iotsitewise.types.environment_variables_map

ExecutionEnvironmentVariables = TypedDict(
    "ExecutionEnvironmentVariables",
    {
        "global": NotRequired[
            "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap"
        ],
        "compute_nodes": NotRequired[
            "capo_iotsitewise.types.compute_node_environment_variables_map.ComputeNodeEnvironmentVariablesMap"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionEnvironmentVariables) -> dict:
    out: dict = {}
    if "global" in value:
        import capo_iotsitewise.types.environment_variables_map

        out["global"] = capo_iotsitewise.types.environment_variables_map.serialize_json(
            value["global"]
        )
    if "compute_nodes" in value:
        import capo_iotsitewise.types.compute_node_environment_variables_map

        out["computeNodes"] = (
            capo_iotsitewise.types.compute_node_environment_variables_map.serialize_json(
                value["compute_nodes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecutionEnvironmentVariables:
    out: ExecutionEnvironmentVariables = {}  # type: ignore[typeddict-item]
    if data.get("global") is not None:
        import capo_iotsitewise.types.environment_variables_map

        out["global"] = (
            capo_iotsitewise.types.environment_variables_map.deserialize_json(
                data["global"]
            )
        )
    if data.get("computeNodes") is not None:
        import capo_iotsitewise.types.compute_node_environment_variables_map

        out["compute_nodes"] = (
            capo_iotsitewise.types.compute_node_environment_variables_map.deserialize_json(
                data["computeNodes"]
            )
        )
    return out

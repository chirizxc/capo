"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionEnvironmentVariablesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.execution_environment_variables_map_key_string
    import capo_iotsitewise.types.execution_environment_variables_map_value_string

ExecutionEnvironmentVariablesMap: TypeAlias = dict[
    "capo_iotsitewise.types.execution_environment_variables_map_key_string.ExecutionEnvironmentVariablesMapKeyString",
    "capo_iotsitewise.types.execution_environment_variables_map_value_string.ExecutionEnvironmentVariablesMapValueString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExecutionEnvironmentVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExecutionEnvironmentVariablesMap:
    out: ExecutionEnvironmentVariablesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out

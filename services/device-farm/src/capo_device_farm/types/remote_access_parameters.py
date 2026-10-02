"""Generated from Smithy shape ``com.amazonaws.devicefarm#RemoteAccessParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.remote_access_parameter_key
    import capo_device_farm.types.remote_access_parameter_value

RemoteAccessParameters: TypeAlias = dict[
    "capo_device_farm.types.remote_access_parameter_key.RemoteAccessParameterKey",
    "capo_device_farm.types.remote_access_parameter_value.RemoteAccessParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RemoteAccessParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoteAccessParameters:
    out: RemoteAccessParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out

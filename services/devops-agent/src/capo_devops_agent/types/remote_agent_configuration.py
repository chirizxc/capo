"""Generated from Smithy shape ``com.amazonaws.devopsagent#RemoteAgentConfiguration``."""

from typing_extensions import TypedDict


class RemoteAgentConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAgentConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoteAgentConfiguration:
    out: RemoteAgentConfiguration = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.devopsagent#RemoteAgentSigV4Configuration``."""

from typing_extensions import TypedDict


class RemoteAgentSigV4Configuration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAgentSigV4Configuration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoteAgentSigV4Configuration:
    out: RemoteAgentSigV4Configuration = {}  # type: ignore[typeddict-item]
    return out

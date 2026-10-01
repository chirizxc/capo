"""Generated from Smithy shape ``com.amazonaws.securityagent#StopThreatModelJobOutput``."""

from typing_extensions import TypedDict


class StopThreatModelJobOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopThreatModelJobOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopThreatModelJobOutput:
    out: StopThreatModelJobOutput = {}  # type: ignore[typeddict-item]
    return out

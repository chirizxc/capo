"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#AgentlessDialerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.dialing_capacity


class AgentlessDialerConfig(TypedDict, closed=True):
    dialing_capacity: NotRequired[
        "capo_connectcampaigns.types.dialing_capacity.DialingCapacity"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AgentlessDialerConfig) -> dict:
    out: dict = {}
    if "dialing_capacity" in value:
        out["dialingCapacity"] = (
            "NaN"
            if value["dialing_capacity"] != value["dialing_capacity"]
            else "Infinity"
            if value["dialing_capacity"] == float("inf")
            else "-Infinity"
            if value["dialing_capacity"] == float("-inf")
            else value["dialing_capacity"]
        )
    return out


def deserialize_json(data: dict) -> AgentlessDialerConfig:
    out: AgentlessDialerConfig = {}  # type: ignore[typeddict-item]
    if data.get("dialingCapacity") is not None:
        out["dialing_capacity"] = float(data["dialingCapacity"])
    return out

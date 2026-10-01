"""Generated from Smithy shape ``com.amazonaws.connect#CrossChannelWorkloadBehavior``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.channel_workload_behavior_type


class CrossChannelWorkloadBehavior(TypedDict, closed=True):
    channel_workload_behavior_type: NotRequired[
        "capo_connect.types.channel_workload_behavior_type.ChannelWorkloadBehaviorType"
    ]
    """<p>Specifies the routing behavior for an agent handling their current channel and workload type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossChannelWorkloadBehavior) -> dict:
    out: dict = {}
    if "channel_workload_behavior_type" in value:
        import capo_connect.types.channel_workload_behavior_type

        out["ChannelWorkloadBehaviorType"] = (
            capo_connect.types.channel_workload_behavior_type.serialize_json(
                value["channel_workload_behavior_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CrossChannelWorkloadBehavior:
    out: CrossChannelWorkloadBehavior = {}  # type: ignore[typeddict-item]
    if data.get("ChannelWorkloadBehaviorType") is not None:
        import capo_connect.types.channel_workload_behavior_type

        out["channel_workload_behavior_type"] = (
            capo_connect.types.channel_workload_behavior_type.deserialize_json(
                data["ChannelWorkloadBehaviorType"]
            )
        )
    return out

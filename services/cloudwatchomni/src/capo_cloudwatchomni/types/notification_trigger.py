"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NotificationTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_state_list


class NotificationTrigger(TypedDict, closed=True):
    state_values: NotRequired[
        "capo_cloudwatchomni.types.alert_state_list.AlertStateList"
    ]
    """Alert state(s) that trigger this rule. Empty / omitted = any state."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NotificationTrigger) -> dict:
    out: dict = {}
    if "state_values" in value:
        import capo_cloudwatchomni.types.alert_state_list

        out["stateValues"] = capo_cloudwatchomni.types.alert_state_list.serialize_cbor(
            value["state_values"]
        )
    return out


def deserialize_cbor(data: dict) -> NotificationTrigger:
    out: NotificationTrigger = {}  # type: ignore[typeddict-item]
    if data.get("stateValues") is not None:
        import capo_cloudwatchomni.types.alert_state_list

        out["state_values"] = (
            capo_cloudwatchomni.types.alert_state_list.deserialize_cbor(
                data["stateValues"]
            )
        )
    return out

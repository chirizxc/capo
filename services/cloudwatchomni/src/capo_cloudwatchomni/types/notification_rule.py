"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NotificationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.notification_target
    import capo_cloudwatchomni.types.notification_trigger


class NotificationRule(TypedDict, closed=True):
    trigger: "capo_cloudwatchomni.types.notification_trigger.NotificationTrigger"
    """The conditions that trigger this notification rule."""
    target: "capo_cloudwatchomni.types.notification_target.NotificationTarget"
    """The destination for notifications from this rule."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NotificationRule) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.notification_trigger

    out["trigger"] = capo_cloudwatchomni.types.notification_trigger.serialize_cbor(
        value["trigger"]
    )
    import capo_cloudwatchomni.types.notification_target

    out["target"] = capo_cloudwatchomni.types.notification_target.serialize_cbor(
        value["target"]
    )
    return out


def deserialize_cbor(data: dict) -> NotificationRule:
    out: NotificationRule = {}  # type: ignore[typeddict-item]
    if data.get("trigger") is not None:
        import capo_cloudwatchomni.types.notification_trigger

        out["trigger"] = (
            capo_cloudwatchomni.types.notification_trigger.deserialize_cbor(
                data["trigger"]
            )
        )
    else:
        raise DeserializationError("NotificationRule.trigger required")
    if data.get("target") is not None:
        import capo_cloudwatchomni.types.notification_target

        out["target"] = capo_cloudwatchomni.types.notification_target.deserialize_cbor(
            data["target"]
        )
    else:
        raise DeserializationError("NotificationRule.target required")
    return out

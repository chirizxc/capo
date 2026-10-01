"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#MessagingLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.long_map


class MessagingLimits(TypedDict, closed=True):
    rate_limits: NotRequired["capo_pinpoint_sms_voice_v2.types.long_map.LongMap"]
    """<p>The maximum send rate for each supported capability, in messages per second. The map is keyed by capability, such as <code>SMS</code>, <code>MMS</code>, <code>VOICE</code>, or <code>RCS</code>.</p>"""
    daily_message_caps: NotRequired["capo_pinpoint_sms_voice_v2.types.long_map.LongMap"]
    """<p>The advisory maximum number of messages that can be sent per day, keyed by provider (for example, <code>T-MOBILE</code>). Applies to 10DLC phone numbers and is omitted when no daily cap applies.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessagingLimits) -> dict:
    out: dict = {}
    if "rate_limits" in value:
        import capo_pinpoint_sms_voice_v2.types.long_map

        out["RateLimits"] = (
            capo_pinpoint_sms_voice_v2.types.long_map.serialize_aws_json_1_0(
                value["rate_limits"]
            )
        )
    if "daily_message_caps" in value:
        import capo_pinpoint_sms_voice_v2.types.long_map

        out["DailyMessageCaps"] = (
            capo_pinpoint_sms_voice_v2.types.long_map.serialize_aws_json_1_0(
                value["daily_message_caps"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MessagingLimits:
    out: MessagingLimits = {}  # type: ignore[typeddict-item]
    if data.get("RateLimits") is not None:
        import capo_pinpoint_sms_voice_v2.types.long_map

        out["rate_limits"] = (
            capo_pinpoint_sms_voice_v2.types.long_map.deserialize_aws_json_1_0(
                data["RateLimits"]
            )
        )
    if data.get("DailyMessageCaps") is not None:
        import capo_pinpoint_sms_voice_v2.types.long_map

        out["daily_message_caps"] = (
            capo_pinpoint_sms_voice_v2.types.long_map.deserialize_aws_json_1_0(
                data["DailyMessageCaps"]
            )
        )
    return out

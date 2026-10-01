"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NotificationRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.notification_rule

NotificationRuleList: TypeAlias = list[
    "capo_cloudwatchomni.types.notification_rule.NotificationRule"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NotificationRuleList) -> list:
    import capo_cloudwatchomni.types.notification_rule

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.notification_rule.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> NotificationRuleList:
    import capo_cloudwatchomni.types.notification_rule

    out: NotificationRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.notification_rule.deserialize_cbor(item))
    return out

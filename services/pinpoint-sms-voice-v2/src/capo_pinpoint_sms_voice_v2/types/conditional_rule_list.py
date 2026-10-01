"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConditionalRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.conditional_rule

ConditionalRuleList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.conditional_rule.ConditionalRule"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionalRuleList) -> list:
    import capo_pinpoint_sms_voice_v2.types.conditional_rule

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.conditional_rule.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConditionalRuleList:
    import capo_pinpoint_sms_voice_v2.types.conditional_rule

    out: ConditionalRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pinpoint_sms_voice_v2.types.conditional_rule.deserialize_aws_json_1_0(
                item
            )
        )
    return out

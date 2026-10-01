"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#FieldConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.field_condition

FieldConditionList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.field_condition.FieldCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FieldConditionList) -> list:
    import capo_pinpoint_sms_voice_v2.types.field_condition

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.field_condition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FieldConditionList:
    import capo_pinpoint_sms_voice_v2.types.field_condition

    out: FieldConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pinpoint_sms_voice_v2.types.field_condition.deserialize_aws_json_1_0(
                item
            )
        )
    return out

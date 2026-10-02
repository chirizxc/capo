"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConditionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.condition_value

ConditionValueList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.condition_value.ConditionValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionValueList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ConditionValueList:
    return [item for item in data if item is not None]

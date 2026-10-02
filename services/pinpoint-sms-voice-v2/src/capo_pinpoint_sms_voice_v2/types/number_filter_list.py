"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.number_filter_value

NumberFilterList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.number_filter_value.NumberFilterValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NumberFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NumberFilterList:
    return [item for item in data if item is not None]

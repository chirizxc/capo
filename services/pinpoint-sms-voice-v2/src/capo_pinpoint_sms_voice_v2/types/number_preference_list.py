"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NumberPreferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.number_preference_item

NumberPreferenceList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.number_preference_item.NumberPreferenceItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NumberPreferenceList) -> list:
    import capo_pinpoint_sms_voice_v2.types.number_preference_item

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.number_preference_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NumberPreferenceList:
    import capo_pinpoint_sms_voice_v2.types.number_preference_item

    out: NumberPreferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pinpoint_sms_voice_v2.types.number_preference_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out

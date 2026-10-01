"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PreferenceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.preference_type

PreferenceTypeList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.preference_type.PreferenceType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferenceTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PreferenceTypeList:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsCarouselCardContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content

RcsCarouselCardContentList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content.RcsCarouselCardContent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsCarouselCardContentList) -> list:
    import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RcsCarouselCardContentList:
    import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content

    out: RcsCarouselCardContentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content.deserialize_aws_json_1_0(
                item
            )
        )
    return out

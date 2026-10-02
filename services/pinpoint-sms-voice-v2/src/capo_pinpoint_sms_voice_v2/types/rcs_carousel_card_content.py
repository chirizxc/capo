"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsCarouselCardContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_card_description
    import capo_pinpoint_sms_voice_v2.types.rcs_card_suggested_action_list
    import capo_pinpoint_sms_voice_v2.types.rcs_card_title
    import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_media


class RcsCarouselCardContent(TypedDict, closed=True):
    title: NotRequired["capo_pinpoint_sms_voice_v2.types.rcs_card_title.RcsCardTitle"]
    """<p>The title of the carousel card. Maximum 200 characters.</p>"""
    description: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_card_description.RcsCardDescription"
    ]
    """<p>The description text of the carousel card. Maximum 2000 characters.</p>"""
    media: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_media.RcsCarouselCardMedia"
    ]
    """<p>The media content of the carousel card. Media height is restricted to SHORT or MEDIUM (TALL is not supported in carousels).</p>"""
    suggestions: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_card_suggested_action_list.RcsCardSuggestedActionList"
    ]
    """<p>Card-level suggested actions for this carousel card. Maximum 4 suggestions per card.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsCarouselCardContent) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "media" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_media

        out["Media"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_media.serialize_aws_json_1_0(
                value["media"]
            )
        )
    if "suggestions" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_card_suggested_action_list

        out["Suggestions"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_card_suggested_action_list.serialize_aws_json_1_0(
                value["suggestions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsCarouselCardContent:
    out: RcsCarouselCardContent = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Media") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_media

        out["media"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_media.deserialize_aws_json_1_0(
                data["Media"]
            )
        )
    if data.get("Suggestions") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_card_suggested_action_list

        out["suggestions"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_card_suggested_action_list.deserialize_aws_json_1_0(
                data["Suggestions"]
            )
        )
    return out

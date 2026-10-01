"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_call_settings
    import capo_socialmessaging.types.whats_app_phone_number_id


class UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    """<p>The unique identifier of the phone number to update. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>.</p>"""
    call_settings: (
        "capo_socialmessaging.types.whats_app_call_settings.WhatsAppCallSettings"
    )
    """<p>The calling settings to apply to the phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput) -> dict:
    out: dict = {}
    import capo_socialmessaging.types.whats_app_call_settings

    out["callSettings"] = (
        capo_socialmessaging.types.whats_app_call_settings.serialize_json(
            value["call_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput:
    out: UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput = {}  # type: ignore[typeddict-item]
    if data.get("callSettings") is not None:
        import capo_socialmessaging.types.whats_app_call_settings

        out["call_settings"] = (
            capo_socialmessaging.types.whats_app_call_settings.deserialize_json(
                data["callSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLinkedWhatsAppBusinessAccountPhoneNumberInput.call_settings required"
        )
    return out

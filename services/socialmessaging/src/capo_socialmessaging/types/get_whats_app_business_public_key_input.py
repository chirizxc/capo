"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppBusinessPublicKeyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_phone_number_id


class GetWhatsAppBusinessPublicKeyInput(TypedDict, closed=True):
    origination_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The unique identifier of the phone number whose business public key to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppBusinessPublicKeyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWhatsAppBusinessPublicKeyInput:
    out: GetWhatsAppBusinessPublicKeyInput = {}  # type: ignore[typeddict-item]
    return out

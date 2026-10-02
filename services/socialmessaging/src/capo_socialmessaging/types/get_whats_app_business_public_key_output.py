"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppBusinessPublicKeyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.business_public_key_pem
    import capo_socialmessaging.types.business_public_key_signature_status


class GetWhatsAppBusinessPublicKeyOutput(TypedDict, closed=True):
    business_public_key: NotRequired[
        "capo_socialmessaging.types.business_public_key_pem.BusinessPublicKeyPem"
    ]
    """<p>The stored PEM-encoded 2048-bit RSA public key.</p>"""
    business_public_key_signature_status: NotRequired[
        "capo_socialmessaging.types.business_public_key_signature_status.BusinessPublicKeySignatureStatus"
    ]
    """<p>The signature status of the stored business public key. Valid values are VALID and MISMATCH.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppBusinessPublicKeyOutput) -> dict:
    out: dict = {}
    if "business_public_key" in value:
        out["businessPublicKey"] = value["business_public_key"]
    if "business_public_key_signature_status" in value:
        out["businessPublicKeySignatureStatus"] = value[
            "business_public_key_signature_status"
        ]
    return out


def deserialize_json(data: dict) -> GetWhatsAppBusinessPublicKeyOutput:
    out: GetWhatsAppBusinessPublicKeyOutput = {}  # type: ignore[typeddict-item]
    if data.get("businessPublicKey") is not None:
        out["business_public_key"] = data["businessPublicKey"]
    if data.get("businessPublicKeySignatureStatus") is not None:
        out["business_public_key_signature_status"] = data[
            "businessPublicKeySignatureStatus"
        ]
    return out

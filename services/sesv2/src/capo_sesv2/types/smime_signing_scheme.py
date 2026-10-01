"""Generated from Smithy shape ``com.amazonaws.sesv2#SmimeSigningScheme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.signature_format


class SmimeSigningScheme(TypedDict, closed=True):
    signature_format: NotRequired["capo_sesv2.types.signature_format.SignatureFormat"]
    """<p>The format of the S/MIME signature that Amazon SES API v2 applies to messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SmimeSigningScheme) -> dict:
    out: dict = {}
    if "signature_format" in value:
        import capo_sesv2.types.signature_format

        out["SignatureFormat"] = capo_sesv2.types.signature_format.serialize_json(
            value["signature_format"]
        )
    return out


def deserialize_json(data: dict) -> SmimeSigningScheme:
    out: SmimeSigningScheme = {}  # type: ignore[typeddict-item]
    if data.get("SignatureFormat") is not None:
        import capo_sesv2.types.signature_format

        out["signature_format"] = capo_sesv2.types.signature_format.deserialize_json(
            data["SignatureFormat"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageSecurityOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.signing_scheme


class MessageSecurityOptions(TypedDict, closed=True):
    signing_scheme: NotRequired["capo_sesv2.types.signing_scheme.SigningScheme"]
    """<p>The signing scheme that Amazon SES API v2 applies to messages sent with the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageSecurityOptions) -> dict:
    out: dict = {}
    if "signing_scheme" in value:
        import capo_sesv2.types.signing_scheme

        out["SigningScheme"] = capo_sesv2.types.signing_scheme.serialize_json(
            value["signing_scheme"]
        )
    return out


def deserialize_json(data: dict) -> MessageSecurityOptions:
    out: MessageSecurityOptions = {}  # type: ignore[typeddict-item]
    if data.get("SigningScheme") is not None:
        import capo_sesv2.types.signing_scheme

        out["signing_scheme"] = capo_sesv2.types.signing_scheme.deserialize_json(
            data["SigningScheme"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sesv2#SignatureFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The format of the S/MIME signature that's applied to a message. The following value is supported:</p> <ul> <li> <p> <code>DETACHED</code> – The signature is carried in a separate MIME part alongside the signed content.</p> </li> </ul>"""
SignatureFormat: TypeAlias = Literal["DETACHED",]


# --- restJson1 ser/de ---
def serialize_json(value: SignatureFormat) -> str:
    return value


def deserialize_json(data: str) -> SignatureFormat:
    return cast(SignatureFormat, data)

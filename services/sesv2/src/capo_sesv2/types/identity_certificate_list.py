"""Generated from Smithy shape ``com.amazonaws.sesv2#IdentityCertificateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.identity_certificate

IdentityCertificateList: TypeAlias = list[
    "capo_sesv2.types.identity_certificate.IdentityCertificate"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCertificateList) -> list:
    import capo_sesv2.types.identity_certificate

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.identity_certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> IdentityCertificateList:
    import capo_sesv2.types.identity_certificate

    out: IdentityCertificateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sesv2.types.identity_certificate.deserialize_json(item))
    return out

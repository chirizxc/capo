"""Generated from Smithy shape ``com.amazonaws.sesv2#IdentityCertificateStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an S/MIME certificate that's associated with an email identity. The status can be one of the following values:</p> <ul> <li> <p> <code>PROVISIONING</code> – The certificate association was created and the certificate is being prepared for use.</p> </li> <li> <p> <code>ACTIVE</code> – The certificate is ready to use for signing.</p> </li> <li> <p> <code>INACTIVE</code> – The certificate is no longer used for signing.</p> </li> <li> <p> <code>DEPROVISIONING</code> – The certificate association is being cleaned up.</p> </li> <li> <p> <code>FAILED</code> – The certificate couldn't be prepared for use, or the certificate has expired.</p> </li> </ul>"""
IdentityCertificateStatus: TypeAlias = Literal[
    "PROVISIONING",
    "INACTIVE",
    "DEPROVISIONING",
    "ACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCertificateStatus) -> str:
    return value


def deserialize_json(data: str) -> IdentityCertificateStatus:
    return cast(IdentityCertificateStatus, data)

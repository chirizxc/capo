"""Generated from Smithy shape ``com.amazonaws.acm#CertificateKeyPairOrigin``."""

from typing import Literal, TypeAlias, cast

"""<p>The origin of the certificate's key pair.</p>"""
CertificateKeyPairOrigin: TypeAlias = Literal[
    "AWS_MANAGED",
    "ACME",
    "CUSTOMER_PROVIDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateKeyPairOrigin) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateKeyPairOrigin:
    return cast(CertificateKeyPairOrigin, data)

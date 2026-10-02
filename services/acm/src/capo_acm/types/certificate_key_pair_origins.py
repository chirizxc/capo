"""Generated from Smithy shape ``com.amazonaws.acm#CertificateKeyPairOrigins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.certificate_key_pair_origin

CertificateKeyPairOrigins: TypeAlias = list[
    "capo_acm.types.certificate_key_pair_origin.CertificateKeyPairOrigin"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateKeyPairOrigins) -> list:
    import capo_acm.types.certificate_key_pair_origin

    out: list = []
    for item in value:
        out.append(
            capo_acm.types.certificate_key_pair_origin.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateKeyPairOrigins:
    import capo_acm.types.certificate_key_pair_origin

    out: CertificateKeyPairOrigins = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_acm.types.certificate_key_pair_origin.deserialize_aws_json_1_1(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.acm#CertificateAuthority``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_acm.types.public_certificate_authority


class _CertificateAuthority_PublicCertificateAuthority(TypedDict, closed=True):
    PublicCertificateAuthority: (
        "capo_acm.types.public_certificate_authority.PublicCertificateAuthority"
    )


CertificateAuthority: TypeAlias = _CertificateAuthority_PublicCertificateAuthority


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthority) -> dict:
    if "PublicCertificateAuthority" in value:
        import capo_acm.types.public_certificate_authority

        return {
            "PublicCertificateAuthority": capo_acm.types.public_certificate_authority.serialize_aws_json_1_1(
                value["PublicCertificateAuthority"]
            )
        }
    else:
        raise SerializationError("CertificateAuthority: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CertificateAuthority:
    if data.get("PublicCertificateAuthority") is not None:
        import capo_acm.types.public_certificate_authority

        return {
            "PublicCertificateAuthority": capo_acm.types.public_certificate_authority.deserialize_aws_json_1_1(
                data["PublicCertificateAuthority"]
            )
        }
    else:
        raise DeserializationError("CertificateAuthority: no recognized variant key")

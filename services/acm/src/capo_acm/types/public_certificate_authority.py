"""Generated from Smithy shape ``com.amazonaws.acm#PublicCertificateAuthority``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.public_key_algorithm_list


class PublicCertificateAuthority(TypedDict, closed=True):
    allowed_key_algorithms: NotRequired[
        "capo_acm.types.public_key_algorithm_list.PublicKeyAlgorithmList"
    ]
    """<p>The key algorithms allowed for certificates issued by this certificate authority.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicCertificateAuthority) -> dict:
    out: dict = {}
    if "allowed_key_algorithms" in value:
        import capo_acm.types.public_key_algorithm_list

        out["AllowedKeyAlgorithms"] = (
            capo_acm.types.public_key_algorithm_list.serialize_aws_json_1_1(
                value["allowed_key_algorithms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicCertificateAuthority:
    out: PublicCertificateAuthority = {}  # type: ignore[typeddict-item]
    if data.get("AllowedKeyAlgorithms") is not None:
        import capo_acm.types.public_key_algorithm_list

        out["allowed_key_algorithms"] = (
            capo_acm.types.public_key_algorithm_list.deserialize_aws_json_1_1(
                data["AllowedKeyAlgorithms"]
            )
        )
    return out

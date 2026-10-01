"""Generated from Smithy shape ``com.amazonaws.acm#PublicKeyAlgorithm``."""

from typing import Literal, TypeAlias, cast

PublicKeyAlgorithm: TypeAlias = Literal[
    "RSA_2048",
    "EC_prime256v1",
    "EC_secp384r1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicKeyAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PublicKeyAlgorithm:
    return cast(PublicKeyAlgorithm, data)

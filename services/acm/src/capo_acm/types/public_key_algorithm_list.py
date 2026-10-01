"""Generated from Smithy shape ``com.amazonaws.acm#PublicKeyAlgorithmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.public_key_algorithm

PublicKeyAlgorithmList: TypeAlias = list[
    "capo_acm.types.public_key_algorithm.PublicKeyAlgorithm"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicKeyAlgorithmList) -> list:
    import capo_acm.types.public_key_algorithm

    out: list = []
    for item in value:
        out.append(capo_acm.types.public_key_algorithm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PublicKeyAlgorithmList:
    import capo_acm.types.public_key_algorithm

    out: PublicKeyAlgorithmList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm.types.public_key_algorithm.deserialize_aws_json_1_1(item))
    return out

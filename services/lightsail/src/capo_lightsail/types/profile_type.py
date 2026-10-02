"""Generated from Smithy shape ``com.amazonaws.lightsail#ProfileType``."""

from typing import Literal, TypeAlias, cast

ProfileType: TypeAlias = Literal[
    "Lightsailor",
    "LightsailPartner",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfileType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProfileType:
    return cast(ProfileType, data)

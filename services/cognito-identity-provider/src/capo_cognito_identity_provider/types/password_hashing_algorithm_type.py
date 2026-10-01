"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PasswordHashingAlgorithmType``."""

from typing import Literal, TypeAlias, cast

PasswordHashingAlgorithmType: TypeAlias = Literal[
    "BCRYPT",
    "SCRYPT",
    "ARGON2ID",
    "PBKDF2_SHA256",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PasswordHashingAlgorithmType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PasswordHashingAlgorithmType:
    return cast(PasswordHashingAlgorithmType, data)

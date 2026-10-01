"""Generated from Smithy shape ``com.amazonaws.iot#InfluxDBSecretType``."""

from typing import Literal, TypeAlias, cast

InfluxDBSecretType: TypeAlias = Literal[
    "SecretString",
    "SecretBinary",
]


# --- restJson1 ser/de ---
def serialize_json(value: InfluxDBSecretType) -> str:
    return value


def deserialize_json(data: str) -> InfluxDBSecretType:
    return cast(InfluxDBSecretType, data)

"""Generated from Smithy shape ``com.amazonaws.kafka#JwtSigningAlgorithm``."""

from typing import Literal, TypeAlias, cast

"""<p>The algorithm used to sign the STS JWT assertion.</p>"""
JwtSigningAlgorithm: TypeAlias = Literal[
    "RS256",
    "ES384",
]


# --- restJson1 ser/de ---
def serialize_json(value: JwtSigningAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> JwtSigningAlgorithm:
    return cast(JwtSigningAlgorithm, data)

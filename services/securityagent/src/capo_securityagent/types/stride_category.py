"""Generated from Smithy shape ``com.amazonaws.securityagent#StrideCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>STRIDE threat classification category.</p>"""
StrideCategory: TypeAlias = Literal[
    "SPOOFING",
    "TAMPERING",
    "REPUDIATION",
    "INFORMATION_DISCLOSURE",
    "DENIAL_OF_SERVICE",
    "ELEVATION_OF_PRIVILEGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StrideCategory) -> str:
    return value


def deserialize_json(data: str) -> StrideCategory:
    return cast(StrideCategory, data)

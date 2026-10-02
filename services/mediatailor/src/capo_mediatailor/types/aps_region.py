"""Generated from Smithy shape ``com.amazonaws.mediatailor#ApsRegion``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported Amazon Publisher Services regions for yield optimization integration. The region selection affects latency and ad inventory availability, so choose the region closest to your primary audience.</p>"""
ApsRegion: TypeAlias = Literal[
    "AMERICAS",
    "EUROPE",
    "ASIA_PACIFIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApsRegion) -> str:
    return value


def deserialize_json(data: str) -> ApsRegion:
    return cast(ApsRegion, data)

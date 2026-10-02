"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Period``."""

from typing import Literal, TypeAlias, cast

"""<p>The time period for rate limiting.</p>"""
Period: TypeAlias = Literal[
    "second",
    "minute",
]


# --- restJson1 ser/de ---
def serialize_json(value: Period) -> str:
    return value


def deserialize_json(data: str) -> Period:
    return cast(Period, data)

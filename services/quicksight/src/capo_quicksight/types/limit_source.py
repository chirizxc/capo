"""Generated from Smithy shape ``com.amazonaws.quicksight#LimitSource``."""

from typing import Literal, TypeAlias, cast

"""<p>The source from which an effective limit was inherited.</p>"""
LimitSource: TypeAlias = Literal[
    "DIRECT_USER",
    "GROUP",
    "ROLE",
    "ACCOUNT",
    "SYSTEM_DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: LimitSource) -> str:
    return value


def deserialize_json(data: str) -> LimitSource:
    return cast(LimitSource, data)

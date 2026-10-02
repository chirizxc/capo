"""Generated from Smithy shape ``com.amazonaws.geoplaces#ZipClassificationCode``."""

from typing import Literal, TypeAlias, cast

ZipClassificationCode: TypeAlias = Literal[
    "Military",
    "PostOfficeBoxes",
    "Unique",
]


# --- restJson1 ser/de ---
def serialize_json(value: ZipClassificationCode) -> str:
    return value


def deserialize_json(data: str) -> ZipClassificationCode:
    return cast(ZipClassificationCode, data)

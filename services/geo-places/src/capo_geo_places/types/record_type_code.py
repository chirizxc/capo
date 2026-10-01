"""Generated from Smithy shape ``com.amazonaws.geoplaces#RecordTypeCode``."""

from typing import Literal, TypeAlias, cast

RecordTypeCode: TypeAlias = Literal[
    "Firm",
    "General",
    "HighRise",
    "PostOfficeBox",
    "Rural",
    "Street",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordTypeCode) -> str:
    return value


def deserialize_json(data: str) -> RecordTypeCode:
    return cast(RecordTypeCode, data)

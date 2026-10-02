"""Generated from Smithy shape ``com.amazonaws.geoplaces#TranslationNameType``."""

from typing import Literal, TypeAlias, cast

TranslationNameType: TypeAlias = Literal[
    "Abbreviation",
    "AreaCode",
    "BaseName",
    "Exonym",
    "Shortened",
    "Synonym",
]


# --- restJson1 ser/de ---
def serialize_json(value: TranslationNameType) -> str:
    return value


def deserialize_json(data: str) -> TranslationNameType:
    return cast(TranslationNameType, data)

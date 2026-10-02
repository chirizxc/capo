"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35Type``."""

from typing import Literal, TypeAlias, cast

"""Scte35 Type"""
Scte35Type: TypeAlias = Literal[
    "NONE",
    "SCTE_35_WITHOUT_SEGMENTATION",
    "SCTE_35_WITHOUT_IDR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35Type) -> str:
    return value


def deserialize_json(data: str) -> Scte35Type:
    return cast(Scte35Type, data)

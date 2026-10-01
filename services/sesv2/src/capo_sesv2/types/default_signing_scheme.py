"""Generated from Smithy shape ``com.amazonaws.sesv2#DefaultSigningScheme``."""

from typing_extensions import TypedDict


class DefaultSigningScheme(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DefaultSigningScheme) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DefaultSigningScheme:
    out: DefaultSigningScheme = {}  # type: ignore[typeddict-item]
    return out

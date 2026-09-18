"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOf__double``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__double
    import capo_pinpoint.types.__string

MapOf__double: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string", "capo_pinpoint.types.__double.__double"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOf__double) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = (
            "NaN"
            if value != value
            else "Infinity"
            if value == float("inf")
            else "-Infinity"
            if value == float("-inf")
            else value
        )
    return out


def deserialize_json(data: dict) -> MapOf__double:
    out: MapOf__double = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out

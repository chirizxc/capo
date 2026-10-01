"""Generated from Smithy shape ``com.amazonaws.kafka#ValueConverter``."""

from typing import Literal, TypeAlias, cast

"""<p>The deserialization format applied to Apache Kafka record values.</p>"""
ValueConverter: TypeAlias = Literal[
    "BYTE_ARRAY",
    "JSON",
    "JSON_SCHEMA_GSR",
    "STRING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValueConverter) -> str:
    return value


def deserialize_json(data: str) -> ValueConverter:
    return cast(ValueConverter, data)

"""Generated from Smithy shape ``com.amazonaws.kafka#IcebergCompressionType``."""

from typing import Literal, TypeAlias, cast

"""<p>Compression codec for Iceberg table data files. Defaults to ZSTD.</p>"""
IcebergCompressionType: TypeAlias = Literal[
    "ZSTD",
    "SNAPPY",
]


# --- restJson1 ser/de ---
def serialize_json(value: IcebergCompressionType) -> str:
    return value


def deserialize_json(data: str) -> IcebergCompressionType:
    return cast(IcebergCompressionType, data)

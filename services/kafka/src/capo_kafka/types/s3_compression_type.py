"""Generated from Smithy shape ``com.amazonaws.kafka#S3CompressionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The compression codec applied to delivered Amazon S3 objects.</p>"""
S3CompressionType: TypeAlias = Literal[
    "NONE",
    "GZIP",
    "ZSTD",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3CompressionType) -> str:
    return value


def deserialize_json(data: str) -> S3CompressionType:
    return cast(S3CompressionType, data)

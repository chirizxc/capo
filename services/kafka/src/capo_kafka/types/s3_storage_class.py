"""Generated from Smithy shape ``com.amazonaws.kafka#S3StorageClass``."""

from typing import Literal, TypeAlias, cast

"""<p>The Amazon S3 storage class applied to delivered objects.</p>"""
S3StorageClass: TypeAlias = Literal[
    "STANDARD",
    "INTELLIGENT_TIERING",
    "GLACIER_IR",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3StorageClass) -> str:
    return value


def deserialize_json(data: str) -> S3StorageClass:
    return cast(S3StorageClass, data)

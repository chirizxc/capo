"""Generated from Smithy shape ``com.amazonaws.iotsitewise#StorageClass``."""

from typing import Literal, TypeAlias, cast

"""<p>The storage type that determines I/O performance characteristics. Family name indicates workload pattern, level number indicates performance within that family.</p>"""
StorageClass: TypeAlias = Literal[
    "STANDARD_1",
    "STANDARD_2",
    "THROUGHPUT_1",
    "THROUGHPUT_2",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    return cast(StorageClass, data)

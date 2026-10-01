"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExportDataType``."""

from typing import Literal, TypeAlias, cast

"""<p>Data types that can be exported from a dataset.</p>"""
ExportDataType: TypeAlias = Literal[
    "VIDEO",
    "TELEMETRY",
    "ANNOTATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportDataType) -> str:
    return value


def deserialize_json(data: str) -> ExportDataType:
    return cast(ExportDataType, data)

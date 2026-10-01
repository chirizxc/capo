"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisLogExportStatus``."""

from typing import Literal, TypeAlias, cast

AnalysisLogExportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisLogExportStatus) -> str:
    return value


def deserialize_json(data: str) -> AnalysisLogExportStatus:
    return cast(AnalysisLogExportStatus, data)

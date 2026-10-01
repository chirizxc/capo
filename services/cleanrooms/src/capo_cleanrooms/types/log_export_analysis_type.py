"""Generated from Smithy shape ``com.amazonaws.cleanrooms#LogExportAnalysisType``."""

from typing import Literal, TypeAlias, cast

LogExportAnalysisType: TypeAlias = Literal["PROTECTED_QUERY",]


# --- restJson1 ser/de ---
def serialize_json(value: LogExportAnalysisType) -> str:
    return value


def deserialize_json(data: str) -> LogExportAnalysisType:
    return cast(LogExportAnalysisType, data)

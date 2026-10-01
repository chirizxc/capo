"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetExportJobStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a dataset export job.</p>"""
DatasetExportJobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "RUNNING",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetExportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetExportJobStatus:
    return cast(DatasetExportJobStatus, data)

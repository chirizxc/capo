"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetExportJobFilter``."""

from typing import Literal, TypeAlias, cast

"""<p>Filter for ListDatasetExportJobs. ALL returns jobs in any status; otherwise returns jobs in the specified status.</p>"""
DatasetExportJobFilter: TypeAlias = Literal[
    "ALL",
    "SUBMITTED",
    "RUNNING",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetExportJobFilter) -> str:
    return value


def deserialize_json(data: str) -> DatasetExportJobFilter:
    return cast(DatasetExportJobFilter, data)

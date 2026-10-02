"""Generated from Smithy shape ``com.amazonaws.iotsitewise#JobType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of enrichment job, derived from the job configuration union member</p>"""
JobType: TypeAlias = Literal["EVENT_DETECTION",]


# --- restJson1 ser/de ---
def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    return cast(JobType, data)

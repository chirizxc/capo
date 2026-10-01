"""Generated from Smithy shape ``com.amazonaws.securityagent#JobType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of pentest job execution.</p>"""
JobType: TypeAlias = Literal[
    "FULL",
    "REVALIDATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    return cast(JobType, data)

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResultDestination``."""

from typing import Literal, TypeAlias, cast

"""Where evaluation results are written: dedicated results log group (default) or the source log group."""
ResultDestination: TypeAlias = Literal[
    "DEDICATED_LOG_GROUP",
    "SOURCE_LOG_GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResultDestination) -> str:
    return value


def deserialize_json(data: str) -> ResultDestination:
    return cast(ResultDestination, data)

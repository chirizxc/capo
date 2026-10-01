"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an agentic retrieval step.</p>"""
AgenticRetrieveStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveStatus) -> str:
    return value


def deserialize_json(data: str) -> AgenticRetrieveStatus:
    return cast(AgenticRetrieveStatus, data)

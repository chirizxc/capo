"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryPersistenceMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether the agent-generated answer is written back to a short-term memory session.</p>"""
AgenticRetrieveMemoryPersistenceMode: TypeAlias = Literal[
    "DEFAULT",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryPersistenceMode) -> str:
    return value


def deserialize_json(data: str) -> AgenticRetrieveMemoryPersistenceMode:
    return cast(AgenticRetrieveMemoryPersistenceMode, data)

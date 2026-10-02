"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a notebook in Amazon SageMaker Unified Studio.</p>"""
NotebookType: TypeAlias = Literal[
    "DATA",
    "SQL",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotebookType) -> str:
    return value


def deserialize_json(data: str) -> NotebookType:
    return cast(NotebookType, data)

"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ProgrammingLanguage``."""

from typing import Literal, TypeAlias, cast

"""<p>The programming language of the instrumentation point. Java, Python, and JavaScript are currently supported.</p>"""
ProgrammingLanguage: TypeAlias = Literal[
    "Java",
    "Python",
    "Javascript",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProgrammingLanguage) -> str:
    return value


def deserialize_json(data: str) -> ProgrammingLanguage:
    return cast(ProgrammingLanguage, data)

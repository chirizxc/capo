"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationErrorCause``."""

from typing import Literal, TypeAlias, cast

"""<p>The reason why applying an instrumentation configuration failed.</p> <ul> <li> <p> <code>FILE_NOT_FOUND</code> - The specified file or file location could not be located.</p> </li> <li> <p> <code>METHOD_NOT_FOUND</code> - The specified method or function does not exist.</p> </li> <li> <p> <code>LINE_NOT_EXECUTABLE</code> - The specified line does not contain executable code.</p> </li> <li> <p> <code>OVERLOADED_METHODS</code> - Multiple overloaded methods were found; provide a line number to disambiguate.</p> </li> <li> <p> <code>LANGUAGE_MISMATCH</code> - The language specified in the configuration does not match the service.</p> </li> <li> <p> <code>RUNTIME_ERROR</code> - A runtime error occurred while applying the instrumentation.</p> </li> </ul>"""
InstrumentationErrorCause: TypeAlias = Literal[
    "FILE_NOT_FOUND",
    "METHOD_NOT_FOUND",
    "LINE_NOT_EXECUTABLE",
    "OVERLOADED_METHODS",
    "LANGUAGE_MISMATCH",
    "RUNTIME_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationErrorCause) -> str:
    return value


def deserialize_json(data: str) -> InstrumentationErrorCause:
    return cast(InstrumentationErrorCause, data)

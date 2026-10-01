"""Generated from Smithy shape ``com.amazonaws.applicationsignals#UnprocessedStatusEventFailureReason``."""

from typing import Literal, TypeAlias, cast

"""<p>The reason an instrumentation status event could not be processed.</p> <ul> <li> <p> <code>THROTTLED</code> - The request exceeded allowed throughput.</p> </li> <li> <p> <code>INTERNAL_ERROR</code> - An internal server error occurred while processing the event.</p> </li> <li> <p> <code>VALIDATION_ERROR</code> - The event failed validation.</p> </li> </ul>"""
UnprocessedStatusEventFailureReason: TypeAlias = Literal[
    "THROTTLED",
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStatusEventFailureReason) -> str:
    return value


def deserialize_json(data: str) -> UnprocessedStatusEventFailureReason:
    return cast(UnprocessedStatusEventFailureReason, data)

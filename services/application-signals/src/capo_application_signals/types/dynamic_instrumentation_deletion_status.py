"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DynamicInstrumentationDeletionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a delete request for an instrumentation configuration. The value is <code>DELETED</code> after a successful deletion.</p>"""
DynamicInstrumentationDeletionStatus: TypeAlias = Literal["DELETED",]


# --- restJson1 ser/de ---
def serialize_json(value: DynamicInstrumentationDeletionStatus) -> str:
    return value


def deserialize_json(data: str) -> DynamicInstrumentationDeletionStatus:
    return cast(DynamicInstrumentationDeletionStatus, data)

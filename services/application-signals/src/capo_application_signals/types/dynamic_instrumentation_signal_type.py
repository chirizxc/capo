"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DynamicInstrumentationSignalType``."""

from typing import Literal, TypeAlias, cast

"""<p>The telemetry signal type for instrumentation.</p> <ul> <li> <p> <code>SNAPSHOT</code> - Captures a snapshot of the instrumentation point.</p> </li> </ul>"""
DynamicInstrumentationSignalType: TypeAlias = Literal["SNAPSHOT",]


# --- restJson1 ser/de ---
def serialize_json(value: DynamicInstrumentationSignalType) -> str:
    return value


def deserialize_json(data: str) -> DynamicInstrumentationSignalType:
    return cast(DynamicInstrumentationSignalType, data)

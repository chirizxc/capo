"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationType``."""

from typing import Literal, TypeAlias, cast

"""Type of instrumentation configuration"""
InstrumentationType: TypeAlias = Literal[
    "BREAKPOINT",
    "PROBE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationType) -> str:
    return value


def deserialize_json(data: str) -> InstrumentationType:
    return cast(InstrumentationType, data)

"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorArnComparison``."""

from typing import Literal, TypeAlias, cast

ConnectorArnComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorArnComparison) -> str:
    return value


def deserialize_json(data: str) -> ConnectorArnComparison:
    return cast(ConnectorArnComparison, data)

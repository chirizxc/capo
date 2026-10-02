"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorTypeComparison``."""

from typing import Literal, TypeAlias, cast

ConnectorTypeComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorTypeComparison) -> str:
    return value


def deserialize_json(data: str) -> ConnectorTypeComparison:
    return cast(ConnectorTypeComparison, data)

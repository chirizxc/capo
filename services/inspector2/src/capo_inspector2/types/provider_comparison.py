"""Generated from Smithy shape ``com.amazonaws.inspector2#ProviderComparison``."""

from typing import Literal, TypeAlias, cast

ProviderComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: ProviderComparison) -> str:
    return value


def deserialize_json(data: str) -> ProviderComparison:
    return cast(ProviderComparison, data)

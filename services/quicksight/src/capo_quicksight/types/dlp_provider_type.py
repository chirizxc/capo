"""Generated from Smithy shape ``com.amazonaws.quicksight#DlpProviderType``."""

from typing import Literal, TypeAlias, cast

DlpProviderType: TypeAlias = Literal["MICROSOFT_PURVIEW",]


# --- restJson1 ser/de ---
def serialize_json(value: DlpProviderType) -> str:
    return value


def deserialize_json(data: str) -> DlpProviderType:
    return cast(DlpProviderType, data)

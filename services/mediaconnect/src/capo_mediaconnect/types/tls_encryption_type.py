"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TlsEncryptionType``."""

from typing import Literal, TypeAlias, cast

TlsEncryptionType: TypeAlias = Literal["PUBLIC",]


# --- restJson1 ser/de ---
def serialize_json(value: TlsEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> TlsEncryptionType:
    return cast(TlsEncryptionType, data)

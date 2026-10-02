"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicTlsEncryptionConfiguration``."""

from typing_extensions import TypedDict


class PublicTlsEncryptionConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PublicTlsEncryptionConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PublicTlsEncryptionConfiguration:
    out: PublicTlsEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    return out

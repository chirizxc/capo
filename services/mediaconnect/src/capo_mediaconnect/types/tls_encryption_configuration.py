"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TlsEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_tls_encryption_configuration


class _TlsEncryptionConfiguration_Public(TypedDict, closed=True):
    Public: "capo_mediaconnect.types.public_tls_encryption_configuration.PublicTlsEncryptionConfiguration"


TlsEncryptionConfiguration: TypeAlias = _TlsEncryptionConfiguration_Public


# --- restJson1 ser/de ---
def serialize_json(value: TlsEncryptionConfiguration) -> dict:
    if "Public" in value:
        import capo_mediaconnect.types.public_tls_encryption_configuration

        return {
            "public": capo_mediaconnect.types.public_tls_encryption_configuration.serialize_json(
                value["Public"]
            )
        }
    else:
        raise SerializationError("TlsEncryptionConfiguration: no variant present")


def deserialize_json(data: dict) -> TlsEncryptionConfiguration:
    if data.get("public") is not None:
        import capo_mediaconnect.types.public_tls_encryption_configuration

        return {
            "Public": capo_mediaconnect.types.public_tls_encryption_configuration.deserialize_json(
                data["public"]
            )
        }
    else:
        raise DeserializationError(
            "TlsEncryptionConfiguration: no recognized variant key"
        )

"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.kms_key_identifier


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_identifier: NotRequired[
        "capo_eventbridgev2.types.kms_key_identifier.KmsKeyIdentifier"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_cbor(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out

"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#EncryptionAtRestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.kms_key_id


class EncryptionAtRestOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p>Specifies the option to enable Encryption At Rest.</p>"""
    kms_key_id: NotRequired["capo_elasticsearch_service.types.kms_key_id.KmsKeyId"]
    """<p> Specifies the KMS Key ID for Encryption At Rest options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAtRestOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> EncryptionAtRestOptions:
    out: EncryptionAtRestOptions = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.macie2#ObjectCountByEncryptionType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__long


class ObjectCountByEncryptionType(TypedDict, closed=True):
    customer_managed: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of objects that are encrypted with customer-provided keys. The objects use server-side encryption with customer-provided keys (SSE-C).</p>"""
    kms_managed: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of objects that are encrypted with KMS keys, either Amazon Web Services managed keys or customer managed keys. The objects use dual-layer server-side encryption or server-side encryption with KMS keys (DSSE-KMS or SSE-KMS).</p>"""
    s3_managed: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of objects that are encrypted with Amazon S3 managed keys. The objects use server-side encryption with Amazon S3 managed keys (SSE-S3).</p>"""
    unencrypted: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of objects that use client-side encryption or aren't encrypted.</p>"""
    unknown: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of objects that Amazon Macie doesn't have current encryption metadata for. Macie can't provide current data about the encryption settings for these objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectCountByEncryptionType) -> dict:
    out: dict = {}
    if "customer_managed" in value:
        out["customerManaged"] = value["customer_managed"]
    if "kms_managed" in value:
        out["kmsManaged"] = value["kms_managed"]
    if "s3_managed" in value:
        out["s3Managed"] = value["s3_managed"]
    if "unencrypted" in value:
        out["unencrypted"] = value["unencrypted"]
    if "unknown" in value:
        out["unknown"] = value["unknown"]
    return out


def deserialize_json(data: dict) -> ObjectCountByEncryptionType:
    out: ObjectCountByEncryptionType = {}  # type: ignore[typeddict-item]
    if data.get("customerManaged") is not None:
        out["customer_managed"] = data["customerManaged"]
    if data.get("kmsManaged") is not None:
        out["kms_managed"] = data["kmsManaged"]
    if data.get("s3Managed") is not None:
        out["s3_managed"] = data["s3Managed"]
    if data.get("unencrypted") is not None:
        out["unencrypted"] = data["unencrypted"]
    if data.get("unknown") is not None:
        out["unknown"] = data["unknown"]
    return out

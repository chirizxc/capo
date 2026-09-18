"""Generated from Smithy shape ``com.amazonaws.licensemanager#IssuerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class IssuerDetails(TypedDict, closed=True):
    name: NotRequired["capo_license_manager.types.string.String"]
    """<p>Issuer name.</p>"""
    sign_key: NotRequired["capo_license_manager.types.string.String"]
    """<p>Asymmetric KMS key from Key Management Service. The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.</p>"""
    key_fingerprint: NotRequired["capo_license_manager.types.string.String"]
    """<p>Issuer key fingerprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssuerDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "sign_key" in value:
        out["SignKey"] = value["sign_key"]
    if "key_fingerprint" in value:
        out["KeyFingerprint"] = value["key_fingerprint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IssuerDetails:
    out: IssuerDetails = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SignKey") is not None:
        out["sign_key"] = data["SignKey"]
    if data.get("KeyFingerprint") is not None:
        out["key_fingerprint"] = data["KeyFingerprint"]
    return out

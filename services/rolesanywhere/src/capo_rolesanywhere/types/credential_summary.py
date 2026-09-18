"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CredentialSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class CredentialSummary(TypedDict, closed=True):
    seen_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 time stamp of when the certificate was last used in a temporary credential request.</p>"""
    serial_number: NotRequired["str"]
    """<p>The serial number of the certificate.</p>"""
    issuer: NotRequired["str"]
    """<p>The fully qualified domain name of the issuing certificate for the presented end-entity certificate.</p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the credential is enabled.</p>"""
    x509_certificate_data: NotRequired["str"]
    """<p>The PEM-encoded data of the certificate.</p>"""
    failed: NotRequired["bool"]
    """<p>Indicates whether the temporary credential request was successful. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CredentialSummary) -> dict:
    out: dict = {}
    if "seen_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["seenAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["seen_at"]
        )
    if "serial_number" in value:
        out["serialNumber"] = value["serial_number"]
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "x509_certificate_data" in value:
        out["x509CertificateData"] = value["x509_certificate_data"]
    if "failed" in value:
        out["failed"] = value["failed"]
    return out


def deserialize_json(data: dict) -> CredentialSummary:
    out: CredentialSummary = {}  # type: ignore[typeddict-item]
    if data.get("seenAt") is not None:
        import datetime

        out["seen_at"] = datetime.datetime.fromisoformat(
            data["seenAt"].replace("Z", "+00:00")
        )
    if data.get("serialNumber") is not None:
        out["serial_number"] = data["serialNumber"]
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("x509CertificateData") is not None:
        out["x509_certificate_data"] = data["x509CertificateData"]
    if data.get("failed") is not None:
        out["failed"] = data["failed"]
    return out

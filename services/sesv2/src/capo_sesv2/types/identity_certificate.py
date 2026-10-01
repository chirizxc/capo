"""Generated from Smithy shape ``com.amazonaws.sesv2#IdentityCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.certificate_arn
    import capo_sesv2.types.email_address
    import capo_sesv2.types.identity_certificate_status
    import capo_sesv2.types.timestamp


class IdentityCertificate(TypedDict, closed=True):
    from_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The email address that the certificate applies to.</p>"""
    status: NotRequired[
        "capo_sesv2.types.identity_certificate_status.IdentityCertificateStatus"
    ]
    """<p>The status of the certificate association. A status of <code>ACTIVE</code> indicates that the certificate is ready to use for signing.</p>"""
    certificate_arn: NotRequired["capo_sesv2.types.certificate_arn.CertificateArn"]
    """<p>The Amazon Resource Name (ARN) of the Certificate Manager (ACM) certificate that's associated with the email identity.</p>"""
    certificate_expiry_time: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp after which the certificate is no longer valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCertificate) -> dict:
    out: dict = {}
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    if "status" in value:
        import capo_sesv2.types.identity_certificate_status

        out["Status"] = capo_sesv2.types.identity_certificate_status.serialize_json(
            value["status"]
        )
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "certificate_expiry_time" in value:
        import capo_sesv2.types.timestamp

        out["CertificateExpiryTime"] = capo_sesv2.types.timestamp.serialize_json(
            value["certificate_expiry_time"]
        )
    return out


def deserialize_json(data: dict) -> IdentityCertificate:
    out: IdentityCertificate = {}  # type: ignore[typeddict-item]
    if data.get("FromAddress") is not None:
        out["from_address"] = data["FromAddress"]
    if data.get("Status") is not None:
        import capo_sesv2.types.identity_certificate_status

        out["status"] = capo_sesv2.types.identity_certificate_status.deserialize_json(
            data["Status"]
        )
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("CertificateExpiryTime") is not None:
        import capo_sesv2.types.timestamp

        out["certificate_expiry_time"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CertificateExpiryTime"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sesv2#ListEmailIdentityCertificatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.identity_certificate_list
    import capo_sesv2.types.next_token


class ListEmailIdentityCertificatesResponse(TypedDict, closed=True):
    certificates: NotRequired[
        "capo_sesv2.types.identity_certificate_list.IdentityCertificateList"
    ]
    """<p>An array that contains the certificate associations for the email identity. Each entry includes the from address, the certificate's status, its Amazon Resource Name (ARN), and its expiry time.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional certificates to list. To view additional certificates, issue another request to <code>ListEmailIdentityCertificates</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEmailIdentityCertificatesResponse) -> dict:
    out: dict = {}
    if "certificates" in value:
        import capo_sesv2.types.identity_certificate_list

        out["Certificates"] = capo_sesv2.types.identity_certificate_list.serialize_json(
            value["certificates"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEmailIdentityCertificatesResponse:
    out: ListEmailIdentityCertificatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Certificates") is not None:
        import capo_sesv2.types.identity_certificate_list

        out["certificates"] = (
            capo_sesv2.types.identity_certificate_list.deserialize_json(
                data["Certificates"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

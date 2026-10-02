"""Generated from Smithy shape ``com.amazonaws.eks#ListCertificateAuthoritiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.certificate_authority_summary_list
    import capo_eks.types.string


class ListCertificateAuthoritiesResponse(TypedDict, closed=True):
    certificate_authorities: NotRequired[
        "capo_eks.types.certificate_authority_summary_list.CertificateAuthoritySummaryList"
    ]
    """<p>A list of certificate authority summary objects, each containing basic information about a certificate authority, including its ID, signing status, and distribution status.</p>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListCertificateAuthorities</code> request. When the results of a <code>ListCertificateAuthorities</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificateAuthoritiesResponse) -> dict:
    out: dict = {}
    if "certificate_authorities" in value:
        import capo_eks.types.certificate_authority_summary_list

        out["certificateAuthorities"] = (
            capo_eks.types.certificate_authority_summary_list.serialize_json(
                value["certificate_authorities"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCertificateAuthoritiesResponse:
    out: ListCertificateAuthoritiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("certificateAuthorities") is not None:
        import capo_eks.types.certificate_authority_summary_list

        out["certificate_authorities"] = (
            capo_eks.types.certificate_authority_summary_list.deserialize_json(
                data["certificateAuthorities"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

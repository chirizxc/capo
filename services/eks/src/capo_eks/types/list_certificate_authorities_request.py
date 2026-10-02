"""Generated from Smithy shape ``com.amazonaws.eks#ListCertificateAuthoritiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.certificate_authority_max_results
    import capo_eks.types.string


class ListCertificateAuthoritiesRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    max_results: NotRequired[
        "capo_eks.types.certificate_authority_max_results.CertificateAuthorityMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value. If you don't specify a value, the default is 100 results.</p>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificateAuthoritiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCertificateAuthoritiesRequest:
    out: ListCertificateAuthoritiesRequest = {}  # type: ignore[typeddict-item]
    return out

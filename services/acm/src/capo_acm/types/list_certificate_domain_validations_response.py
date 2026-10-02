"""Generated from Smithy shape ``com.amazonaws.acm#ListCertificateDomainValidationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.domain_validation_summary_list
    import capo_acm.types.next_token


class ListCertificateDomainValidationsResponse(TypedDict, closed=True):
    domain_validation_summary_list: NotRequired[
        "capo_acm.types.domain_validation_summary_list.DomainValidationSummaryList"
    ]
    """<p>A list of <a>DomainValidationSummary</a> objects, one for each domain on the certificate. Each object contains the domain name and its active and requested validation configurations.</p>"""
    next_token: NotRequired["capo_acm.types.next_token.NextToken"]
    """<p>If the number of results exceeds <code>MaxItems</code>, this token is included in the response. Use this token in a subsequent <code>ListCertificateDomainValidations</code> request to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificateDomainValidationsResponse) -> dict:
    out: dict = {}
    if "domain_validation_summary_list" in value:
        import capo_acm.types.domain_validation_summary_list

        out["DomainValidationSummaryList"] = (
            capo_acm.types.domain_validation_summary_list.serialize_aws_json_1_1(
                value["domain_validation_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificateDomainValidationsResponse:
    out: ListCertificateDomainValidationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainValidationSummaryList") is not None:
        import capo_acm.types.domain_validation_summary_list

        out["domain_validation_summary_list"] = (
            capo_acm.types.domain_validation_summary_list.deserialize_aws_json_1_1(
                data["DomainValidationSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

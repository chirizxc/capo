"""Generated from Smithy shape ``com.amazonaws.acm#DescribeAcmeDomainValidationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_domain_validation


class DescribeAcmeDomainValidationResponse(TypedDict, closed=True):
    acme_domain_validation: NotRequired[
        "capo_acm.types.acme_domain_validation.AcmeDomainValidation"
    ]
    """<p>The ACME domain validation details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAcmeDomainValidationResponse) -> dict:
    out: dict = {}
    if "acme_domain_validation" in value:
        import capo_acm.types.acme_domain_validation

        out["AcmeDomainValidation"] = (
            capo_acm.types.acme_domain_validation.serialize_aws_json_1_1(
                value["acme_domain_validation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAcmeDomainValidationResponse:
    out: DescribeAcmeDomainValidationResponse = {}  # type: ignore[typeddict-item]
    if data.get("AcmeDomainValidation") is not None:
        import capo_acm.types.acme_domain_validation

        out["acme_domain_validation"] = (
            capo_acm.types.acme_domain_validation.deserialize_aws_json_1_1(
                data["AcmeDomainValidation"]
            )
        )
    return out

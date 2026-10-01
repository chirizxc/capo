"""Generated from Smithy shape ``com.amazonaws.acm#ListAcmeDomainValidationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_domain_validation_list


class ListAcmeDomainValidationsResponse(TypedDict, closed=True):
    acme_domain_validations: NotRequired[
        "capo_acm.types.acme_domain_validation_list.AcmeDomainValidationList"
    ]
    """<p>The list of domain validations.</p>"""
    next_token: NotRequired["str"]
    """<p>A token for pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcmeDomainValidationsResponse) -> dict:
    out: dict = {}
    if "acme_domain_validations" in value:
        import capo_acm.types.acme_domain_validation_list

        out["AcmeDomainValidations"] = (
            capo_acm.types.acme_domain_validation_list.serialize_aws_json_1_1(
                value["acme_domain_validations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcmeDomainValidationsResponse:
    out: ListAcmeDomainValidationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AcmeDomainValidations") is not None:
        import capo_acm.types.acme_domain_validation_list

        out["acme_domain_validations"] = (
            capo_acm.types.acme_domain_validation_list.deserialize_aws_json_1_1(
                data["AcmeDomainValidations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

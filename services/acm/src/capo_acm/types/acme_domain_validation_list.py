"""Generated from Smithy shape ``com.amazonaws.acm#AcmeDomainValidationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.acme_domain_validation_summary

AcmeDomainValidationList: TypeAlias = list[
    "capo_acm.types.acme_domain_validation_summary.AcmeDomainValidationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeDomainValidationList) -> list:
    import capo_acm.types.acme_domain_validation_summary

    out: list = []
    for item in value:
        out.append(
            capo_acm.types.acme_domain_validation_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AcmeDomainValidationList:
    import capo_acm.types.acme_domain_validation_summary

    out: AcmeDomainValidationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_acm.types.acme_domain_validation_summary.deserialize_aws_json_1_1(item)
        )
    return out

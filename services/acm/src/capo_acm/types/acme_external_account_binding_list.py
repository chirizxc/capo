"""Generated from Smithy shape ``com.amazonaws.acm#AcmeExternalAccountBindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.acme_external_account_binding_summary

AcmeExternalAccountBindingList: TypeAlias = list[
    "capo_acm.types.acme_external_account_binding_summary.AcmeExternalAccountBindingSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeExternalAccountBindingList) -> list:
    import capo_acm.types.acme_external_account_binding_summary

    out: list = []
    for item in value:
        out.append(
            capo_acm.types.acme_external_account_binding_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AcmeExternalAccountBindingList:
    import capo_acm.types.acme_external_account_binding_summary

    out: AcmeExternalAccountBindingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_acm.types.acme_external_account_binding_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out

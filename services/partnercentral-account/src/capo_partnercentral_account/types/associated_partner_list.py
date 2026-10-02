"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AssociatedPartnerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.qualifications_association_partner

AssociatedPartnerList: TypeAlias = list[
    "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociatedPartnerList) -> list:
    import capo_partnercentral_account.types.qualifications_association_partner

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_account.types.qualifications_association_partner.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AssociatedPartnerList:
    import capo_partnercentral_account.types.qualifications_association_partner

    out: AssociatedPartnerList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_account.types.qualifications_association_partner.deserialize_aws_json_1_0(
                item
            )
        )
    return out

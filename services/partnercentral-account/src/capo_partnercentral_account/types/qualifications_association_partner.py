"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#QualificationsAssociationPartner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.aws_account_id
    import capo_partnercentral_account.types.partner_profile_id


class QualificationsAssociationPartner(TypedDict, closed=True):
    profile_id: NotRequired[
        "capo_partnercentral_account.types.partner_profile_id.PartnerProfileId"
    ]
    """<p>The unique identifier for the partner profile, in the format <code>pprofile-*</code>. Required in requests if <code>AccountId</code> is not provided.</p>"""
    account_id: NotRequired[
        "capo_partnercentral_account.types.aws_account_id.AwsAccountId"
    ]
    """<p>The 12-digit AWS account ID linked to the partner profile. Required in requests if <code>ProfileId</code> is not provided.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QualificationsAssociationPartner) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> QualificationsAssociationPartner:
    out: QualificationsAssociationPartner = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out

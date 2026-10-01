"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServicePolicyDisassociatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.policy_disassociation_reason
    import capo_resiliencehubv2.types.policy_value_source


class ServicePolicyDisassociatedMetadata(TypedDict, closed=True):
    policy_name: NotRequired["str"]
    """<p>The name of the disassociated policy.</p>"""
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    policy_owner_account_id: NotRequired["str"]
    """<p>The account that owns the policy.</p>"""
    policy_source: NotRequired[
        "capo_resiliencehubv2.types.policy_value_source.PolicyValueSource"
    ]
    """<p>The source of the policy.</p> <ul> <li> <p>SELF — the policy belongs to the account that owns the service.</p> </li> <li> <p>CROSS_ACCOUNT — the policy belongs to another account and was shared with the organization.</p> </li> </ul>"""
    reason: NotRequired[
        "capo_resiliencehubv2.types.policy_disassociation_reason.PolicyDisassociationReason"
    ]
    """<p>The reason the policy was disassociated from the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServicePolicyDisassociatedMetadata) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "policy_owner_account_id" in value:
        out["policyOwnerAccountId"] = value["policy_owner_account_id"]
    if "policy_source" in value:
        import capo_resiliencehubv2.types.policy_value_source

        out["policySource"] = (
            capo_resiliencehubv2.types.policy_value_source.serialize_json(
                value["policy_source"]
            )
        )
    if "reason" in value:
        import capo_resiliencehubv2.types.policy_disassociation_reason

        out["reason"] = (
            capo_resiliencehubv2.types.policy_disassociation_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServicePolicyDisassociatedMetadata:
    out: ServicePolicyDisassociatedMetadata = {}  # type: ignore[typeddict-item]
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("policyOwnerAccountId") is not None:
        out["policy_owner_account_id"] = data["policyOwnerAccountId"]
    if data.get("policySource") is not None:
        import capo_resiliencehubv2.types.policy_value_source

        out["policy_source"] = (
            capo_resiliencehubv2.types.policy_value_source.deserialize_json(
                data["policySource"]
            )
        )
    if data.get("reason") is not None:
        import capo_resiliencehubv2.types.policy_disassociation_reason

        out["reason"] = (
            capo_resiliencehubv2.types.policy_disassociation_reason.deserialize_json(
                data["reason"]
            )
        )
    return out

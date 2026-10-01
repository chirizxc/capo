"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServicePolicyAssociatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.policy_value_source


class ServicePolicyAssociatedMetadata(TypedDict, closed=True):
    policy_name: NotRequired["str"]
    """<p>The name of the associated policy.</p>"""
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    policy_owner_account_id: NotRequired["str"]
    """<p>The account that owns the policy.</p>"""
    policy_source: NotRequired[
        "capo_resiliencehubv2.types.policy_value_source.PolicyValueSource"
    ]
    """<p>The source of the policy.</p> <ul> <li> <p>SELF — the policy belongs to the account that owns the service.</p> </li> <li> <p>CROSS_ACCOUNT — the policy belongs to another account and was shared with the organization.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServicePolicyAssociatedMetadata) -> dict:
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
    return out


def deserialize_json(data: dict) -> ServicePolicyAssociatedMetadata:
    out: ServicePolicyAssociatedMetadata = {}  # type: ignore[typeddict-item]
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
    return out

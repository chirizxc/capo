"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateApprovalPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.applicable_to
    import capo_quicksight.types.approval_group_list
    import capo_quicksight.types.asset_type_list
    import capo_quicksight.types.governed_action_list
    import capo_quicksight.types.policy_description
    import capo_quicksight.types.policy_id
    import capo_quicksight.types.policy_name


class UpdateApprovalPolicyRequest(TypedDict, closed=True):
    policy_id: "capo_quicksight.types.policy_id.PolicyId"
    """<p>The unique identifier of the approval policy to update.</p>"""
    name: NotRequired["capo_quicksight.types.policy_name.PolicyName"]
    """<p>The name of the approval policy.</p>"""
    description: NotRequired[
        "capo_quicksight.types.policy_description.PolicyDescription"
    ]
    """<p>A description of the approval policy.</p>"""
    actions: NotRequired[
        "capo_quicksight.types.governed_action_list.GovernedActionList"
    ]
    """<p>The list of governed actions that trigger the approval workflow.</p>"""
    asset_types: NotRequired["capo_quicksight.types.asset_type_list.AssetTypeList"]
    """<p>The list of asset types that the approval policy applies to.</p>"""
    applicable_to: NotRequired["capo_quicksight.types.applicable_to.ApplicableTo"]
    """<p>The scoping configuration that determines who the approval policy applies to.</p>"""
    approval_groups: NotRequired[
        "capo_quicksight.types.approval_group_list.ApprovalGroupList"
    ]
    """<p>The list of group ARNs whose members can approve requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApprovalPolicyRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "actions" in value:
        import capo_quicksight.types.governed_action_list

        out["Actions"] = capo_quicksight.types.governed_action_list.serialize_json(
            value["actions"]
        )
    if "asset_types" in value:
        import capo_quicksight.types.asset_type_list

        out["AssetTypes"] = capo_quicksight.types.asset_type_list.serialize_json(
            value["asset_types"]
        )
    if "applicable_to" in value:
        import capo_quicksight.types.applicable_to

        out["ApplicableTo"] = capo_quicksight.types.applicable_to.serialize_json(
            value["applicable_to"]
        )
    if "approval_groups" in value:
        import capo_quicksight.types.approval_group_list

        out["ApprovalGroups"] = (
            capo_quicksight.types.approval_group_list.serialize_json(
                value["approval_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApprovalPolicyRequest:
    out: UpdateApprovalPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Actions") is not None:
        import capo_quicksight.types.governed_action_list

        out["actions"] = capo_quicksight.types.governed_action_list.deserialize_json(
            data["Actions"]
        )
    if data.get("AssetTypes") is not None:
        import capo_quicksight.types.asset_type_list

        out["asset_types"] = capo_quicksight.types.asset_type_list.deserialize_json(
            data["AssetTypes"]
        )
    if data.get("ApplicableTo") is not None:
        import capo_quicksight.types.applicable_to

        out["applicable_to"] = capo_quicksight.types.applicable_to.deserialize_json(
            data["ApplicableTo"]
        )
    if data.get("ApprovalGroups") is not None:
        import capo_quicksight.types.approval_group_list

        out["approval_groups"] = (
            capo_quicksight.types.approval_group_list.deserialize_json(
                data["ApprovalGroups"]
            )
        )
    return out

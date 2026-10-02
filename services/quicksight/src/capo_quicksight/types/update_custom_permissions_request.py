"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateCustomPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.capabilities
    import capo_quicksight.types.custom_permissions_name
    import capo_quicksight.types.governance


class UpdateCustomPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the custom permissions profile that you want to update.</p>"""
    custom_permissions_name: (
        "capo_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions profile that you want to update.</p>"""
    capabilities: NotRequired["capo_quicksight.types.capabilities.Capabilities"]
    """<p>A set of actions to include in the custom permissions profile.</p>"""
    governance: NotRequired["capo_quicksight.types.governance.Governance"]
    """<p>The governance configuration for the custom permissions profile. The <code>UpdateCustomPermissions</code> operation replaces all existing <code>Capabilities</code> and <code>Governance</code> values. If you omit this parameter, Amazon Quick removes governance from the profile and the existing custom permission behavior applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomPermissionsRequest) -> dict:
    out: dict = {}
    if "capabilities" in value:
        import capo_quicksight.types.capabilities

        out["Capabilities"] = capo_quicksight.types.capabilities.serialize_json(
            value["capabilities"]
        )
    if "governance" in value:
        import capo_quicksight.types.governance

        out["Governance"] = capo_quicksight.types.governance.serialize_json(
            value["governance"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCustomPermissionsRequest:
    out: UpdateCustomPermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Capabilities") is not None:
        import capo_quicksight.types.capabilities

        out["capabilities"] = capo_quicksight.types.capabilities.deserialize_json(
            data["Capabilities"]
        )
    if data.get("Governance") is not None:
        import capo_quicksight.types.governance

        out["governance"] = capo_quicksight.types.governance.deserialize_json(
            data["Governance"]
        )
    return out

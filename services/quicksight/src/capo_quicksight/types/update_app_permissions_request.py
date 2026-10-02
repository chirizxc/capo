"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAppPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.app_id
    import capo_quicksight.types.app_visibility
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.resource_permission_list


class UpdateAppPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the app.</p>"""
    app_id: "capo_quicksight.types.app_id.AppId"
    """<p>The ID of the app.</p>"""
    grant_permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions that you want to grant on the app.</p>"""
    revoke_permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions that you want to revoke from the app.</p>"""
    visibility: NotRequired["capo_quicksight.types.app_visibility.AppVisibility"]
    """<p>The visibility to set for the app. Currently, only <code>PRIVATE</code> is accepted, which removes public (anonymous) access from the app. If you don't specify a value, the app's visibility is unchanged. Setting an app to <code>PUBLIC</code> through this operation is not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppPermissionsRequest) -> dict:
    out: dict = {}
    if "grant_permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["GrantPermissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["grant_permissions"]
            )
        )
    if "revoke_permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["RevokePermissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["revoke_permissions"]
            )
        )
    if "visibility" in value:
        import capo_quicksight.types.app_visibility

        out["Visibility"] = capo_quicksight.types.app_visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAppPermissionsRequest:
    out: UpdateAppPermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("GrantPermissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["grant_permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["GrantPermissions"]
            )
        )
    if data.get("RevokePermissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["revoke_permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["RevokePermissions"]
            )
        )
    if data.get("Visibility") is not None:
        import capo_quicksight.types.app_visibility

        out["visibility"] = capo_quicksight.types.app_visibility.deserialize_json(
            data["Visibility"]
        )
    return out

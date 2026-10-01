"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAppPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.app_id
    import capo_quicksight.types.resource_permission_list


class DescribeAppPermissionsResponse(TypedDict, closed=True):
    app_id: NotRequired["capo_quicksight.types.app_id.AppId"]
    """<p>The ID of the app.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the app.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The resource permissions for the app.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppPermissionsResponse) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["AppId"] = value["app_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAppPermissionsResponse:
    out: DescribeAppPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppId") is not None:
        out["app_id"] = data["AppId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Permissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out

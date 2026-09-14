"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppPermissionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.permissions_output_list


class UpdateQAppPermissionsOutput(TypedDict, closed=True):
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Q App for which permissions were updated.</p>"""
    app_id: NotRequired["str"]
    """<p>The unique identifier of the Amazon Q App for which permissions were updated.</p>"""
    permissions: NotRequired[
        "capo_qapps.types.permissions_output_list.PermissionsOutputList"
    ]
    """<p>The updated list of permissions for the Amazon Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppPermissionsOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "permissions" in value:
        import capo_qapps.types.permissions_output_list

        out["permissions"] = capo_qapps.types.permissions_output_list.serialize_json(
            value["permissions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateQAppPermissionsOutput:
    out: UpdateQAppPermissionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    if data.get("permissions") is not None:
        import capo_qapps.types.permissions_output_list

        out["permissions"] = capo_qapps.types.permissions_output_list.deserialize_json(
            data["permissions"]
        )
    return out

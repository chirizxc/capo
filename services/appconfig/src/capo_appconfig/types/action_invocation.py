"""Generated from Smithy shape ``com.amazonaws.appconfig#ActionInvocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.arn
    import capo_appconfig.types.id
    import capo_appconfig.types.identifier
    import capo_appconfig.types.name
    import capo_appconfig.types.string
    import capo_appconfig.types.uri


class ActionInvocation(TypedDict, closed=True):
    extension_identifier: NotRequired["capo_appconfig.types.identifier.Identifier"]
    """<p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>"""
    action_name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The name of the action.</p>"""
    uri: NotRequired["capo_appconfig.types.uri.Uri"]
    """<p>The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.</p>"""
    role_arn: NotRequired["capo_appconfig.types.arn.Arn"]
    """<p>An Amazon Resource Name (ARN) for an Identity and Access Management assume role.</p>"""
    error_message: NotRequired["capo_appconfig.types.string.String"]
    """<p>The error message when an extension invocation fails.</p>"""
    error_code: NotRequired["capo_appconfig.types.string.String"]
    """<p>The error code when an extension invocation fails.</p>"""
    invocation_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>A system-generated ID for this invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionInvocation) -> dict:
    out: dict = {}
    if "extension_identifier" in value:
        out["ExtensionIdentifier"] = value["extension_identifier"]
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    if "uri" in value:
        out["Uri"] = value["uri"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "invocation_id" in value:
        out["InvocationId"] = value["invocation_id"]
    return out


def deserialize_json(data: dict) -> ActionInvocation:
    out: ActionInvocation = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionIdentifier") is not None:
        out["extension_identifier"] = data["ExtensionIdentifier"]
    if data.get("ActionName") is not None:
        out["action_name"] = data["ActionName"]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("InvocationId") is not None:
        out["invocation_id"] = data["InvocationId"]
    return out

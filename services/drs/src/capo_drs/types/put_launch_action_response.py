"""Generated from Smithy shape ``com.amazonaws.drs#PutLaunchActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_action_category
    import capo_drs.types.launch_action_description
    import capo_drs.types.launch_action_id
    import capo_drs.types.launch_action_name
    import capo_drs.types.launch_action_order
    import capo_drs.types.launch_action_parameters
    import capo_drs.types.launch_action_resource_id
    import capo_drs.types.launch_action_type
    import capo_drs.types.launch_action_version
    import capo_drs.types.ssm_document_name


class PutLaunchActionResponse(TypedDict, closed=True):
    resource_id: NotRequired[
        "capo_drs.types.launch_action_resource_id.LaunchActionResourceId"
    ]
    action_id: NotRequired["capo_drs.types.launch_action_id.LaunchActionId"]
    action_code: NotRequired["capo_drs.types.ssm_document_name.SsmDocumentName"]
    """<p>Launch action code.</p>"""
    type: NotRequired["capo_drs.types.launch_action_type.LaunchActionType"]
    """<p>Launch action type.</p>"""
    name: NotRequired["capo_drs.types.launch_action_name.LaunchActionName"]
    active: NotRequired["bool"]
    """<p>Whether the launch action is active.</p>"""
    order: NotRequired["capo_drs.types.launch_action_order.LaunchActionOrder"]
    action_version: NotRequired[
        "capo_drs.types.launch_action_version.LaunchActionVersion"
    ]
    optional: NotRequired["bool"]
    """<p>Whether the launch will not be marked as failed if this action fails.</p>"""
    parameters: NotRequired[
        "capo_drs.types.launch_action_parameters.LaunchActionParameters"
    ]
    description: NotRequired[
        "capo_drs.types.launch_action_description.LaunchActionDescription"
    ]
    category: NotRequired["capo_drs.types.launch_action_category.LaunchActionCategory"]


# --- restJson1 ser/de ---
def serialize_json(value: PutLaunchActionResponse) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "action_code" in value:
        out["actionCode"] = value["action_code"]
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "active" in value:
        out["active"] = value["active"]
    if "order" in value:
        out["order"] = value["order"]
    if "action_version" in value:
        out["actionVersion"] = value["action_version"]
    if "optional" in value:
        out["optional"] = value["optional"]
    if "parameters" in value:
        import capo_drs.types.launch_action_parameters

        out["parameters"] = capo_drs.types.launch_action_parameters.serialize_json(
            value["parameters"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    return out


def deserialize_json(data: dict) -> PutLaunchActionResponse:
    out: PutLaunchActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    if data.get("actionCode") is not None:
        out["action_code"] = data["actionCode"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("active") is not None:
        out["active"] = data["active"]
    if data.get("order") is not None:
        out["order"] = data["order"]
    if data.get("actionVersion") is not None:
        out["action_version"] = data["actionVersion"]
    if data.get("optional") is not None:
        out["optional"] = data["optional"]
    if data.get("parameters") is not None:
        import capo_drs.types.launch_action_parameters

        out["parameters"] = capo_drs.types.launch_action_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    return out

"""Generated from Smithy shape ``com.amazonaws.drs#PutLaunchActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.launch_action_category
    import capo_drs.types.launch_action_description
    import capo_drs.types.launch_action_id
    import capo_drs.types.launch_action_name
    import capo_drs.types.launch_action_order
    import capo_drs.types.launch_action_parameters
    import capo_drs.types.launch_action_resource_id
    import capo_drs.types.launch_action_version
    import capo_drs.types.ssm_document_name


class PutLaunchActionRequest(TypedDict, closed=True):
    resource_id: "capo_drs.types.launch_action_resource_id.LaunchActionResourceId"
    action_code: "capo_drs.types.ssm_document_name.SsmDocumentName"
    """<p>Launch action code.</p>"""
    order: "capo_drs.types.launch_action_order.LaunchActionOrder"
    action_id: "capo_drs.types.launch_action_id.LaunchActionId"
    optional: "bool"
    """<p>Whether the launch will not be marked as failed if this action fails.</p>"""
    active: "bool"
    """<p>Whether the launch action is active.</p>"""
    name: "capo_drs.types.launch_action_name.LaunchActionName"
    action_version: "capo_drs.types.launch_action_version.LaunchActionVersion"
    category: "capo_drs.types.launch_action_category.LaunchActionCategory"
    parameters: NotRequired[
        "capo_drs.types.launch_action_parameters.LaunchActionParameters"
    ]
    description: "capo_drs.types.launch_action_description.LaunchActionDescription"


# --- restJson1 ser/de ---
def serialize_json(value: PutLaunchActionRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    out["actionCode"] = value["action_code"]
    out["order"] = value["order"]
    out["actionId"] = value["action_id"]
    out["optional"] = value["optional"]
    out["active"] = value["active"]
    out["name"] = value["name"]
    out["actionVersion"] = value["action_version"]
    out["category"] = value["category"]
    if "parameters" in value:
        import capo_drs.types.launch_action_parameters

        out["parameters"] = capo_drs.types.launch_action_parameters.serialize_json(
            value["parameters"]
        )
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PutLaunchActionRequest:
    out: PutLaunchActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("PutLaunchActionRequest.resource_id required")
    if data.get("actionCode") is not None:
        out["action_code"] = data["actionCode"]
    else:
        raise DeserializationError("PutLaunchActionRequest.action_code required")
    if data.get("order") is not None:
        out["order"] = data["order"]
    else:
        raise DeserializationError("PutLaunchActionRequest.order required")
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        raise DeserializationError("PutLaunchActionRequest.action_id required")
    if data.get("optional") is not None:
        out["optional"] = data["optional"]
    else:
        raise DeserializationError("PutLaunchActionRequest.optional required")
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        raise DeserializationError("PutLaunchActionRequest.active required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutLaunchActionRequest.name required")
    if data.get("actionVersion") is not None:
        out["action_version"] = data["actionVersion"]
    else:
        raise DeserializationError("PutLaunchActionRequest.action_version required")
    if data.get("category") is not None:
        out["category"] = data["category"]
    else:
        raise DeserializationError("PutLaunchActionRequest.category required")
    if data.get("parameters") is not None:
        import capo_drs.types.launch_action_parameters

        out["parameters"] = capo_drs.types.launch_action_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("PutLaunchActionRequest.description required")
    return out

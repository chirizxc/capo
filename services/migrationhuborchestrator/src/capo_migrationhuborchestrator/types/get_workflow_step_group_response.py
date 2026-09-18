"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetWorkflowStepGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_migrationhuborchestrator.types.owner
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.step_group_status
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.tools_list


class GetWorkflowStepGroupResponse(TypedDict, closed=True):
    id: NotRequired["capo_migrationhuborchestrator.types.step_group_id.StepGroupId"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the step group.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.step_group_status.StepGroupStatus"
    ]
    """<p>The status of the step group.</p>"""
    owner: NotRequired["capo_migrationhuborchestrator.types.owner.Owner"]
    """<p>The owner of the step group.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group was created.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group was last modified.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group ended.</p>"""
    tools: NotRequired["capo_migrationhuborchestrator.types.tools_list.ToolsList"]
    """<p>List of AWS services utilized in a migration workflow.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step group.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepGroupResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "creation_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["lastModifiedTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "end_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["endTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "tools" in value:
        import capo_migrationhuborchestrator.types.tools_list

        out["tools"] = capo_migrationhuborchestrator.types.tools_list.serialize_json(
            value["tools"]
        )
    if "previous" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "next" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    return out


def deserialize_json(data: dict) -> GetWorkflowStepGroupResponse:
    out: GetWorkflowStepGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    if data.get("creationTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("lastModifiedTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["end_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if data.get("tools") is not None:
        import capo_migrationhuborchestrator.types.tools_list

        out["tools"] = capo_migrationhuborchestrator.types.tools_list.deserialize_json(
            data["tools"]
        )
    if data.get("previous") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if data.get("next") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.deserialize_json(
            data["next"]
        )
    return out

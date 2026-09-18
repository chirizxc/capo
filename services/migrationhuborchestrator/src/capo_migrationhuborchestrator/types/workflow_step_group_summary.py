"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.owner
    import capo_migrationhuborchestrator.types.step_group_status
    import capo_migrationhuborchestrator.types.string_list


class WorkflowStepGroupSummary(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step group.</p>"""
    owner: NotRequired["capo_migrationhuborchestrator.types.owner.Owner"]
    """<p>The owner of the step group.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.step_group_status.StepGroupStatus"
    ]
    """<p>The status of the step group.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step group.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepGroupSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "status" in value:
        out["status"] = value["status"]
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


def deserialize_json(data: dict) -> WorkflowStepGroupSummary:
    out: WorkflowStepGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    if data.get("status") is not None:
        out["status"] = data["status"]
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

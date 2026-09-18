"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetWorkflowStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_migrationhuborchestrator.types.owner
    import capo_migrationhuborchestrator.types.step_action_type
    import capo_migrationhuborchestrator.types.step_status
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.workflow_step_automation_configuration
    import capo_migrationhuborchestrator.types.workflow_step_output_list


class GetWorkflowStepResponse(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""
    step_group_id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    step_id: NotRequired["str"]
    """<p>The ID of the step.</p>"""
    description: NotRequired["str"]
    """<p>The description of the step.</p>"""
    step_action_type: NotRequired[
        "capo_migrationhuborchestrator.types.step_action_type.StepActionType"
    ]
    """<p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>"""
    owner: NotRequired["capo_migrationhuborchestrator.types.owner.Owner"]
    """<p>The owner of the step.</p>"""
    workflow_step_automation_configuration: NotRequired[
        "capo_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
    ]
    """<p>The custom script to run tests on source or target environments.</p>"""
    step_target: NotRequired[
        "capo_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The servers on which a step will be run.</p>"""
    outputs: NotRequired[
        "capo_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
    ]
    """<p>The outputs of the step.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step.</p>"""
    status: NotRequired["capo_migrationhuborchestrator.types.step_status.StepStatus"]
    """<p>The status of the step.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the migration workflow.</p>"""
    script_output_location: NotRequired["str"]
    """<p>The output location of the script.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step was created.</p>"""
    last_start_time: NotRequired["datetime.datetime"]
    """<p>The time at which the workflow was last started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step ended.</p>"""
    no_of_srv_completed: NotRequired["int"]
    """<p>The number of servers that have been migrated.</p>"""
    no_of_srv_failed: NotRequired["int"]
    """<p>The number of servers that have failed to migrate.</p>"""
    total_no_of_srv: NotRequired["int"]
    """<p>The total number of servers that have been migrated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "step_group_id" in value:
        out["stepGroupId"] = value["step_group_id"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "step_action_type" in value:
        out["stepActionType"] = value["step_action_type"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "workflow_step_automation_configuration" in value:
        import capo_migrationhuborchestrator.types.workflow_step_automation_configuration

        out["workflowStepAutomationConfiguration"] = (
            capo_migrationhuborchestrator.types.workflow_step_automation_configuration.serialize_json(
                value["workflow_step_automation_configuration"]
            )
        )
    if "step_target" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["stepTarget"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["step_target"]
            )
        )
    if "outputs" in value:
        import capo_migrationhuborchestrator.types.workflow_step_output_list

        out["outputs"] = (
            capo_migrationhuborchestrator.types.workflow_step_output_list.serialize_json(
                value["outputs"]
            )
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
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "script_output_location" in value:
        out["scriptOutputLocation"] = value["script_output_location"]
    if "creation_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_start_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["lastStartTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_start_time"]
            )
        )
    if "end_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["endTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "no_of_srv_completed" in value:
        out["noOfSrvCompleted"] = value["no_of_srv_completed"]
    if "no_of_srv_failed" in value:
        out["noOfSrvFailed"] = value["no_of_srv_failed"]
    if "total_no_of_srv" in value:
        out["totalNoOfSrv"] = value["total_no_of_srv"]
    return out


def deserialize_json(data: dict) -> GetWorkflowStepResponse:
    out: GetWorkflowStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("stepGroupId") is not None:
        out["step_group_id"] = data["stepGroupId"]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("stepActionType") is not None:
        out["step_action_type"] = data["stepActionType"]
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    if data.get("workflowStepAutomationConfiguration") is not None:
        import capo_migrationhuborchestrator.types.workflow_step_automation_configuration

        out["workflow_step_automation_configuration"] = (
            capo_migrationhuborchestrator.types.workflow_step_automation_configuration.deserialize_json(
                data["workflowStepAutomationConfiguration"]
            )
        )
    if data.get("stepTarget") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["step_target"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["stepTarget"]
            )
        )
    if data.get("outputs") is not None:
        import capo_migrationhuborchestrator.types.workflow_step_output_list

        out["outputs"] = (
            capo_migrationhuborchestrator.types.workflow_step_output_list.deserialize_json(
                data["outputs"]
            )
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
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("scriptOutputLocation") is not None:
        out["script_output_location"] = data["scriptOutputLocation"]
    if data.get("creationTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("lastStartTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["last_start_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastStartTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["end_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if data.get("noOfSrvCompleted") is not None:
        out["no_of_srv_completed"] = data["noOfSrvCompleted"]
    if data.get("noOfSrvFailed") is not None:
        out["no_of_srv_failed"] = data["noOfSrvFailed"]
    if data.get("totalNoOfSrv") is not None:
        out["total_no_of_srv"] = data["totalNoOfSrv"]
    return out

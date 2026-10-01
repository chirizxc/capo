"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetThreatModelJobTasksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.task_id_list
    import capo_securityagent.types.threat_model_job_task_list


class BatchGetThreatModelJobTasksOutput(TypedDict, closed=True):
    threat_model_job_tasks: NotRequired[
        "capo_securityagent.types.threat_model_job_task_list.ThreatModelJobTaskList"
    ]
    """<p>The list of threat model job tasks that were found.</p>"""
    not_found: NotRequired["capo_securityagent.types.task_id_list.TaskIdList"]
    """<p>The list of task identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetThreatModelJobTasksOutput) -> dict:
    out: dict = {}
    if "threat_model_job_tasks" in value:
        import capo_securityagent.types.threat_model_job_task_list

        out["threatModelJobTasks"] = (
            capo_securityagent.types.threat_model_job_task_list.serialize_json(
                value["threat_model_job_tasks"]
            )
        )
    if "not_found" in value:
        import capo_securityagent.types.task_id_list

        out["notFound"] = capo_securityagent.types.task_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetThreatModelJobTasksOutput:
    out: BatchGetThreatModelJobTasksOutput = {}  # type: ignore[typeddict-item]
    if data.get("threatModelJobTasks") is not None:
        import capo_securityagent.types.threat_model_job_task_list

        out["threat_model_job_tasks"] = (
            capo_securityagent.types.threat_model_job_task_list.deserialize_json(
                data["threatModelJobTasks"]
            )
        )
    if data.get("notFound") is not None:
        import capo_securityagent.types.task_id_list

        out["not_found"] = capo_securityagent.types.task_id_list.deserialize_json(
            data["notFound"]
        )
    return out

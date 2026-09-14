"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.ecs_task_details
    import capo_guardduty.types.integer
    import capo_guardduty.types.string
    import capo_guardduty.types.tags


class EcsClusterDetails(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the ECS Cluster.</p>"""
    arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the cluster.</p>"""
    status: NotRequired["capo_guardduty.types.string.String"]
    """<p>The status of the ECS cluster.</p>"""
    active_services_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of services that are running on the cluster in an ACTIVE state.</p>"""
    registered_container_instances_count: NotRequired[
        "capo_guardduty.types.integer.Integer"
    ]
    """<p>The number of container instances registered into the cluster.</p>"""
    running_tasks_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of tasks in the cluster that are in the RUNNING state.</p>"""
    tags: NotRequired["capo_guardduty.types.tags.Tags"]
    """<p>The tags of the ECS Cluster.</p>"""
    task_details: NotRequired["capo_guardduty.types.ecs_task_details.EcsTaskDetails"]
    """<p>Contains information about the details of the ECS Task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsClusterDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "active_services_count" in value:
        out["activeServicesCount"] = value["active_services_count"]
    if "registered_container_instances_count" in value:
        out["registeredContainerInstancesCount"] = value[
            "registered_container_instances_count"
        ]
    if "running_tasks_count" in value:
        out["runningTasksCount"] = value["running_tasks_count"]
    if "tags" in value:
        import capo_guardduty.types.tags

        out["tags"] = capo_guardduty.types.tags.serialize_json(value["tags"])
    if "task_details" in value:
        import capo_guardduty.types.ecs_task_details

        out["taskDetails"] = capo_guardduty.types.ecs_task_details.serialize_json(
            value["task_details"]
        )
    return out


def deserialize_json(data: dict) -> EcsClusterDetails:
    out: EcsClusterDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("activeServicesCount") is not None:
        out["active_services_count"] = data["activeServicesCount"]
    if data.get("registeredContainerInstancesCount") is not None:
        out["registered_container_instances_count"] = data[
            "registeredContainerInstancesCount"
        ]
    if data.get("runningTasksCount") is not None:
        out["running_tasks_count"] = data["runningTasksCount"]
    if data.get("tags") is not None:
        import capo_guardduty.types.tags

        out["tags"] = capo_guardduty.types.tags.deserialize_json(data["tags"])
    if data.get("taskDetails") is not None:
        import capo_guardduty.types.ecs_task_details

        out["task_details"] = capo_guardduty.types.ecs_task_details.deserialize_json(
            data["taskDetails"]
        )
    return out

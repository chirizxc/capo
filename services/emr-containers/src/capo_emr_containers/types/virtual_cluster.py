"""Generated from Smithy shape ``com.amazonaws.emrcontainers#VirtualCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.boolean
    import capo_emr_containers.types.container_provider
    import capo_emr_containers.types.date
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.scheduler_configuration
    import capo_emr_containers.types.scheduler_status
    import capo_emr_containers.types.tag_map
    import capo_emr_containers.types.virtual_cluster_arn
    import capo_emr_containers.types.virtual_cluster_state


class VirtualCluster(TypedDict, closed=True):
    id: NotRequired["capo_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The ID of the virtual cluster.</p>"""
    name: NotRequired[
        "capo_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the virtual cluster.</p>"""
    arn: NotRequired["capo_emr_containers.types.virtual_cluster_arn.VirtualClusterArn"]
    """<p>The ARN of the virtual cluster.</p>"""
    state: NotRequired[
        "capo_emr_containers.types.virtual_cluster_state.VirtualClusterState"
    ]
    """<p>The state of the virtual cluster.</p>"""
    container_provider: NotRequired[
        "capo_emr_containers.types.container_provider.ContainerProvider"
    ]
    """<p>The container provider of the virtual cluster.</p>"""
    created_at: NotRequired["capo_emr_containers.types.date.Date"]
    """<p>The date and time when the virtual cluster is created.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The assigned tags of the virtual cluster.</p>"""
    security_configuration_id: NotRequired[
        "capo_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>The ID of the security configuration.</p>"""
    session_enabled: NotRequired["capo_emr_containers.types.boolean.Boolean"]
    """<p>Specifies whether the virtual cluster has session support enabled. </p>"""
    scheduler_configuration: NotRequired[
        "capo_emr_containers.types.scheduler_configuration.SchedulerConfiguration"
    ]
    """<p>The scheduler configuration (concurrency and queue limits) applied to the virtual cluster. The service does not return this field when no scheduler limits are configured.</p>"""
    scheduler_status: NotRequired[
        "capo_emr_containers.types.scheduler_status.SchedulerStatus"
    ]
    """<p>The current in-queue and concurrent job-run counts for the virtual cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualCluster) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "state" in value:
        import capo_emr_containers.types.virtual_cluster_state

        out["state"] = capo_emr_containers.types.virtual_cluster_state.serialize_json(
            value["state"]
        )
    if "container_provider" in value:
        import capo_emr_containers.types.container_provider

        out["containerProvider"] = (
            capo_emr_containers.types.container_provider.serialize_json(
                value["container_provider"]
            )
        )
    if "created_at" in value:
        import capo_emr_containers.types.date

        out["createdAt"] = capo_emr_containers.types.date.serialize_json(
            value["created_at"]
        )
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    if "security_configuration_id" in value:
        out["securityConfigurationId"] = value["security_configuration_id"]
    if "session_enabled" in value:
        out["sessionEnabled"] = value["session_enabled"]
    if "scheduler_configuration" in value:
        import capo_emr_containers.types.scheduler_configuration

        out["schedulerConfiguration"] = (
            capo_emr_containers.types.scheduler_configuration.serialize_json(
                value["scheduler_configuration"]
            )
        )
    if "scheduler_status" in value:
        import capo_emr_containers.types.scheduler_status

        out["schedulerStatus"] = (
            capo_emr_containers.types.scheduler_status.serialize_json(
                value["scheduler_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualCluster:
    out: VirtualCluster = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("state") is not None:
        import capo_emr_containers.types.virtual_cluster_state

        out["state"] = capo_emr_containers.types.virtual_cluster_state.deserialize_json(
            data["state"]
        )
    if data.get("containerProvider") is not None:
        import capo_emr_containers.types.container_provider

        out["container_provider"] = (
            capo_emr_containers.types.container_provider.deserialize_json(
                data["containerProvider"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_emr_containers.types.date

        out["created_at"] = capo_emr_containers.types.date.deserialize_json(
            data["createdAt"]
        )
    if data.get("tags") is not None:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    if data.get("securityConfigurationId") is not None:
        out["security_configuration_id"] = data["securityConfigurationId"]
    if data.get("sessionEnabled") is not None:
        out["session_enabled"] = data["sessionEnabled"]
    if data.get("schedulerConfiguration") is not None:
        import capo_emr_containers.types.scheduler_configuration

        out["scheduler_configuration"] = (
            capo_emr_containers.types.scheduler_configuration.deserialize_json(
                data["schedulerConfiguration"]
            )
        )
    if data.get("schedulerStatus") is not None:
        import capo_emr_containers.types.scheduler_status

        out["scheduler_status"] = (
            capo_emr_containers.types.scheduler_status.deserialize_json(
                data["schedulerStatus"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoPatchConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_patch_schedule_details
    import capo_sagemaker.types.cluster_patching_strategy
    import capo_sagemaker.types.deployment_configuration


class ClusterAutoPatchConfigDetails(TypedDict, closed=True):
    patching_strategy: NotRequired[
        "capo_sagemaker.types.cluster_patching_strategy.ClusterPatchingStrategy"
    ]
    """<p>The strategy used for applying patches to instances in the group.</p> <ul> <li> <p> <code>WhenIdle</code>: Cordons all instances and patches each instance as it becomes idle (no running jobs). Each instance is uncordoned immediately after patching and becomes available for new jobs. If instances do not become idle, they remain on the previous AMI version. You can then use UpdateClusterSoftware with the desired ImageReleaseVersion to manually update the remaining instances.</p> </li> <li> <p> <code>WhenAllIdle</code>: Cordons all instances and waits for all to become idle before patching. All instances are uncordoned after patching completes. If not all instances become idle, no patching occurs and all instances remain on the previous AMI version.</p> </li> </ul>"""
    current_patch_schedule: NotRequired[
        "capo_sagemaker.types.cluster_patch_schedule_details.ClusterPatchScheduleDetails"
    ]
    """<p>The currently active patch schedule that the system will execute.</p>"""
    desired_patch_schedule: NotRequired[
        "capo_sagemaker.types.cluster_patch_schedule_details.ClusterPatchScheduleDetails"
    ]
    """<p>The requested patch schedule. Differs from CurrentPatchSchedule when a reschedule request is pending.</p>"""
    deployment_config: NotRequired[
        "capo_sagemaker.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>The deployment configuration for rolling patch updates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAutoPatchConfigDetails) -> dict:
    out: dict = {}
    if "patching_strategy" in value:
        import capo_sagemaker.types.cluster_patching_strategy

        out["PatchingStrategy"] = (
            capo_sagemaker.types.cluster_patching_strategy.serialize_aws_json_1_1(
                value["patching_strategy"]
            )
        )
    if "current_patch_schedule" in value:
        import capo_sagemaker.types.cluster_patch_schedule_details

        out["CurrentPatchSchedule"] = (
            capo_sagemaker.types.cluster_patch_schedule_details.serialize_aws_json_1_1(
                value["current_patch_schedule"]
            )
        )
    if "desired_patch_schedule" in value:
        import capo_sagemaker.types.cluster_patch_schedule_details

        out["DesiredPatchSchedule"] = (
            capo_sagemaker.types.cluster_patch_schedule_details.serialize_aws_json_1_1(
                value["desired_patch_schedule"]
            )
        )
    if "deployment_config" in value:
        import capo_sagemaker.types.deployment_configuration

        out["DeploymentConfig"] = (
            capo_sagemaker.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterAutoPatchConfigDetails:
    out: ClusterAutoPatchConfigDetails = {}  # type: ignore[typeddict-item]
    if data.get("PatchingStrategy") is not None:
        import capo_sagemaker.types.cluster_patching_strategy

        out["patching_strategy"] = (
            capo_sagemaker.types.cluster_patching_strategy.deserialize_aws_json_1_1(
                data["PatchingStrategy"]
            )
        )
    if data.get("CurrentPatchSchedule") is not None:
        import capo_sagemaker.types.cluster_patch_schedule_details

        out["current_patch_schedule"] = (
            capo_sagemaker.types.cluster_patch_schedule_details.deserialize_aws_json_1_1(
                data["CurrentPatchSchedule"]
            )
        )
    if data.get("DesiredPatchSchedule") is not None:
        import capo_sagemaker.types.cluster_patch_schedule_details

        out["desired_patch_schedule"] = (
            capo_sagemaker.types.cluster_patch_schedule_details.deserialize_aws_json_1_1(
                data["DesiredPatchSchedule"]
            )
        )
    if data.get("DeploymentConfig") is not None:
        import capo_sagemaker.types.deployment_configuration

        out["deployment_config"] = (
            capo_sagemaker.types.deployment_configuration.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    return out

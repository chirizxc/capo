"""Generated from Smithy shape ``com.amazonaws.batch#UpdateManagedInstancesProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.infrastructure_optimization
    import capo_batch.types.instance_launch_template_update
    import capo_batch.types.string


class UpdateManagedInstancesProviderConfiguration(TypedDict, closed=True):
    propagate_tags: NotRequired["capo_batch.types.string.String"]
    """<p>Specifies whether tags on the capacity provider are propagated to the Amazon EC2 instances it launches. Valid values:</p> <ul> <li> <p> <code>CAPACITY_PROVIDER</code> — Propagates tags to instances.</p> </li> <li> <p> <code>NONE</code> — Does not propagate tags to instances.</p> </li> </ul>"""
    infrastructure_role_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The updated Amazon Resource Name (ARN) of the IAM role that Amazon ECS assumes to manage Amazon EC2 instances on your behalf.</p>"""
    instance_launch_template: NotRequired[
        "capo_batch.types.instance_launch_template_update.InstanceLaunchTemplateUpdate"
    ]
    """<p>The updated instance launch configuration for the Amazon ECS Managed Instances capacity provider.</p>"""
    infrastructure_optimization: NotRequired[
        "capo_batch.types.infrastructure_optimization.InfrastructureOptimization"
    ]
    """<p>The updated infrastructure optimization configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateManagedInstancesProviderConfiguration) -> dict:
    out: dict = {}
    if "propagate_tags" in value:
        out["propagateTags"] = value["propagate_tags"]
    if "infrastructure_role_arn" in value:
        out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "instance_launch_template" in value:
        import capo_batch.types.instance_launch_template_update

        out["instanceLaunchTemplate"] = (
            capo_batch.types.instance_launch_template_update.serialize_json(
                value["instance_launch_template"]
            )
        )
    if "infrastructure_optimization" in value:
        import capo_batch.types.infrastructure_optimization

        out["infrastructureOptimization"] = (
            capo_batch.types.infrastructure_optimization.serialize_json(
                value["infrastructure_optimization"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateManagedInstancesProviderConfiguration:
    out: UpdateManagedInstancesProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("propagateTags") is not None:
        out["propagate_tags"] = data["propagateTags"]
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    if data.get("instanceLaunchTemplate") is not None:
        import capo_batch.types.instance_launch_template_update

        out["instance_launch_template"] = (
            capo_batch.types.instance_launch_template_update.deserialize_json(
                data["instanceLaunchTemplate"]
            )
        )
    if data.get("infrastructureOptimization") is not None:
        import capo_batch.types.infrastructure_optimization

        out["infrastructure_optimization"] = (
            capo_batch.types.infrastructure_optimization.deserialize_json(
                data["infrastructureOptimization"]
            )
        )
    return out

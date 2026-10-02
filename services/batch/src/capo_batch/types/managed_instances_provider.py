"""Generated from Smithy shape ``com.amazonaws.batch#ManagedInstancesProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.infrastructure_optimization
    import capo_batch.types.instance_launch_template
    import capo_batch.types.string


class ManagedInstancesProvider(TypedDict, closed=True):
    propagate_tags: NotRequired["capo_batch.types.string.String"]
    """<p>Specifies whether tags on the capacity provider are propagated to the Amazon EC2 instances it launches. Valid values:</p> <ul> <li> <p> <code>CAPACITY_PROVIDER</code> — Propagates tags to instances.</p> </li> <li> <p> <code>NONE</code> (default) — Does not propagate tags to instances.</p> </li> </ul>"""
    infrastructure_role_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon ECS assumes to manage Amazon EC2 instances on your behalf. This role must have a trust policy for <code>ecs.amazonaws.com</code>. You must have the <code>iam:PassRole</code> permission for this role with the condition <code>iam:PassedToService: ecs.amazonaws.com</code>.</p>"""
    instance_launch_template: NotRequired[
        "capo_batch.types.instance_launch_template.InstanceLaunchTemplate"
    ]
    """<p>The instance launch configuration for the Amazon ECS Managed Instances capacity provider. Contains networking, instance profile, instance requirements, capacity type, storage, and monitoring configuration.</p>"""
    infrastructure_optimization: NotRequired[
        "capo_batch.types.infrastructure_optimization.InfrastructureOptimization"
    ]
    """<p>The infrastructure optimization configuration for the capacity provider. Specifies the idle-instance scale-in behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedInstancesProvider) -> dict:
    out: dict = {}
    if "propagate_tags" in value:
        out["propagateTags"] = value["propagate_tags"]
    if "infrastructure_role_arn" in value:
        out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "instance_launch_template" in value:
        import capo_batch.types.instance_launch_template

        out["instanceLaunchTemplate"] = (
            capo_batch.types.instance_launch_template.serialize_json(
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


def deserialize_json(data: dict) -> ManagedInstancesProvider:
    out: ManagedInstancesProvider = {}  # type: ignore[typeddict-item]
    if data.get("propagateTags") is not None:
        out["propagate_tags"] = data["propagateTags"]
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    if data.get("instanceLaunchTemplate") is not None:
        import capo_batch.types.instance_launch_template

        out["instance_launch_template"] = (
            capo_batch.types.instance_launch_template.deserialize_json(
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

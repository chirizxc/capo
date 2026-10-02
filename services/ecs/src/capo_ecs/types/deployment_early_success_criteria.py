"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentEarlySuccessCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.healthy_percent_integer
    import capo_ecs.types.service_revision_cleanup


class DeploymentEarlySuccessCriteria(TypedDict, closed=True):
    enable: "capo_ecs.types.boolean.Boolean"
    """<p>Specifies whether to use the early success criteria for the service deployment. When set to <code>false</code>, the deployment uses the default behavior, where Amazon ECS considers the deployment successful when the target service revision fully stabilizes and the previous tasks are removed. The default value is <code>false</code>.</p> <p>When set to <code>true</code>, Amazon ECS monitors the deployment to meet early success criteria. You must also specify <code>healthyPercent</code> and <code>sourceServiceRevisionCleanup</code>.</p>"""
    healthy_percent: NotRequired[
        "capo_ecs.types.healthy_percent_integer.HealthyPercentInteger"
    ]
    """<p>The percentage of healthy tasks that the target service revision must reach before Amazon ECS considers the deployment successful. This percentage is relative to the service's <code>desiredCount</code> and must be an integer between <code>0</code> and <code>100</code>. This value must be greater than or equal to the <code>minimumHealthyPercent</code> value.</p> <p>After this percentage of tasks is healthy and the bake time elapses, Amazon ECS completes the deployment. Amazon ECS continues to scale the target service revision to 100 percent in the background.</p>"""
    source_service_revision_cleanup: NotRequired[
        "capo_ecs.types.service_revision_cleanup.ServiceRevisionCleanup"
    ]
    """<p>The time when Amazon ECS removes the source revisions' tasks relative to deployment completion. The valid values are:</p> <ul> <li> <p> <code>BLOCKING</code>—Amazon ECS removes the previous tasks before it marks the deployment as successful.</p> </li> <li> <p> <code>DEFERRED</code>—Amazon ECS marks the deployment successful, and then removes the previous tasks in the background.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentEarlySuccessCriteria) -> dict:
    out: dict = {}
    out["enable"] = value.get("enable", False)
    if "healthy_percent" in value:
        out["healthyPercent"] = value["healthy_percent"]
    if "source_service_revision_cleanup" in value:
        import capo_ecs.types.service_revision_cleanup

        out["sourceServiceRevisionCleanup"] = (
            capo_ecs.types.service_revision_cleanup.serialize_aws_json_1_1(
                value["source_service_revision_cleanup"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentEarlySuccessCriteria:
    out: DeploymentEarlySuccessCriteria = {}  # type: ignore[typeddict-item]
    if data.get("enable") is not None:
        out["enable"] = data["enable"]
    else:
        out["enable"] = False
    if data.get("healthyPercent") is not None:
        out["healthy_percent"] = data["healthyPercent"]
    if data.get("sourceServiceRevisionCleanup") is not None:
        import capo_ecs.types.service_revision_cleanup

        out["source_service_revision_cleanup"] = (
            capo_ecs.types.service_revision_cleanup.deserialize_aws_json_1_1(
                data["sourceServiceRevisionCleanup"]
            )
        )
    return out

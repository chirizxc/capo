"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonCapacityProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.integer
    import capo_ecs.types.string


class DaemonCapacityProvider(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    running_count: "capo_ecs.types.integer.Integer"
    """<p>The number of daemon tasks running on this capacity provider.</p>"""
    without_daemon_count: "capo_ecs.types.integer.Integer"
    """<p>The number of instances on this capacity provider that are running without the daemon task. This applies to daemons that aren't critical, where the instance remains available for your other tasks even if the daemon task can't start or stops. These instances aren't included in <code>runningCount</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonCapacityProvider) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    out["runningCount"] = value.get("running_count", 0)
    out["withoutDaemonCount"] = value.get("without_daemon_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonCapacityProvider:
    out: DaemonCapacityProvider = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("runningCount") is not None:
        out["running_count"] = data["runningCount"]
    else:
        out["running_count"] = 0
    if data.get("withoutDaemonCount") is not None:
        out["without_daemon_count"] = data["withoutDaemonCount"]
    else:
        out["without_daemon_count"] = 0
    return out

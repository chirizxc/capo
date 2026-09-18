"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesWorkloadDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean
    import capo_guardduty.types.containers
    import capo_guardduty.types.string
    import capo_guardduty.types.volumes


class KubernetesWorkloadDetails(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>Kubernetes workload name.</p>"""
    type: NotRequired["capo_guardduty.types.string.String"]
    """<p>Kubernetes workload type (e.g. Pod, Deployment, etc.).</p>"""
    uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>Kubernetes workload ID.</p>"""
    namespace: NotRequired["capo_guardduty.types.string.String"]
    """<p>Kubernetes namespace that the workload is part of.</p>"""
    host_network: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Whether the hostNetwork flag is enabled for the pods included in the workload.</p>"""
    service_account_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The service account name that is associated with a Kubernetes workload.</p>"""
    containers: NotRequired["capo_guardduty.types.containers.Containers"]
    """<p>Containers running as part of the Kubernetes workload.</p>"""
    volumes: NotRequired["capo_guardduty.types.volumes.Volumes"]
    """<p>Volumes used by the Kubernetes workload.</p>"""
    host_ipc: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Whether the host IPC flag is enabled for the pods in the workload.</p>"""
    host_pid: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Whether the host PID flag is enabled for the pods in the workload. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesWorkloadDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "uid" in value:
        out["uid"] = value["uid"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "host_network" in value:
        out["hostNetwork"] = value["host_network"]
    if "service_account_name" in value:
        out["serviceAccountName"] = value["service_account_name"]
    if "containers" in value:
        import capo_guardduty.types.containers

        out["containers"] = capo_guardduty.types.containers.serialize_json(
            value["containers"]
        )
    if "volumes" in value:
        import capo_guardduty.types.volumes

        out["volumes"] = capo_guardduty.types.volumes.serialize_json(value["volumes"])
    if "host_ipc" in value:
        out["hostIPC"] = value["host_ipc"]
    if "host_pid" in value:
        out["hostPID"] = value["host_pid"]
    return out


def deserialize_json(data: dict) -> KubernetesWorkloadDetails:
    out: KubernetesWorkloadDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("hostNetwork") is not None:
        out["host_network"] = data["hostNetwork"]
    if data.get("serviceAccountName") is not None:
        out["service_account_name"] = data["serviceAccountName"]
    if data.get("containers") is not None:
        import capo_guardduty.types.containers

        out["containers"] = capo_guardduty.types.containers.deserialize_json(
            data["containers"]
        )
    if data.get("volumes") is not None:
        import capo_guardduty.types.volumes

        out["volumes"] = capo_guardduty.types.volumes.deserialize_json(data["volumes"])
    if data.get("hostIPC") is not None:
        out["host_ipc"] = data["hostIPC"]
    if data.get("hostPID") is not None:
        out["host_pid"] = data["hostPID"]
    return out

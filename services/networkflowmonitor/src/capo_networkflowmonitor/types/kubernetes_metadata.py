"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#KubernetesMetadata``."""

from typing_extensions import NotRequired, TypedDict


class KubernetesMetadata(TypedDict, closed=True):
    local_service_name: NotRequired["str"]
    """<p>The service name for a local resource.</p>"""
    local_pod_name: NotRequired["str"]
    """<p>The name of the pod for a local resource.</p>"""
    local_pod_namespace: NotRequired["str"]
    """<p>The namespace of the pod for a local resource.</p>"""
    remote_service_name: NotRequired["str"]
    """<p>The service name for a remote resource.</p>"""
    remote_pod_name: NotRequired["str"]
    """<p>The name of the pod for a remote resource.</p>"""
    remote_pod_namespace: NotRequired["str"]
    """<p>The namespace of the pod for a remote resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesMetadata) -> dict:
    out: dict = {}
    if "local_service_name" in value:
        out["localServiceName"] = value["local_service_name"]
    if "local_pod_name" in value:
        out["localPodName"] = value["local_pod_name"]
    if "local_pod_namespace" in value:
        out["localPodNamespace"] = value["local_pod_namespace"]
    if "remote_service_name" in value:
        out["remoteServiceName"] = value["remote_service_name"]
    if "remote_pod_name" in value:
        out["remotePodName"] = value["remote_pod_name"]
    if "remote_pod_namespace" in value:
        out["remotePodNamespace"] = value["remote_pod_namespace"]
    return out


def deserialize_json(data: dict) -> KubernetesMetadata:
    out: KubernetesMetadata = {}  # type: ignore[typeddict-item]
    if data.get("localServiceName") is not None:
        out["local_service_name"] = data["localServiceName"]
    if data.get("localPodName") is not None:
        out["local_pod_name"] = data["localPodName"]
    if data.get("localPodNamespace") is not None:
        out["local_pod_namespace"] = data["localPodNamespace"]
    if data.get("remoteServiceName") is not None:
        out["remote_service_name"] = data["remoteServiceName"]
    if data.get("remotePodName") is not None:
        out["remote_pod_name"] = data["remotePodName"]
    if data.get("remotePodNamespace") is not None:
        out["remote_pod_namespace"] = data["remotePodNamespace"]
    return out

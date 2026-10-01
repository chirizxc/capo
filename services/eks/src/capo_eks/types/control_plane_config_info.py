"""Generated from Smithy shape ``com.amazonaws.eks#ControlPlaneConfigInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.kube_api_server_version_config
    import capo_eks.types.kube_controller_manager_version_config
    import capo_eks.types.kube_scheduler_version_config


class ControlPlaneConfigInfo(TypedDict, closed=True):
    kube_api_server_config: NotRequired[
        "capo_eks.types.kube_api_server_version_config.KubeApiServerVersionConfig"
    ]
    """<p>The Kubernetes API server configuration defaults and constraints.</p>"""
    kube_scheduler_config: NotRequired[
        "capo_eks.types.kube_scheduler_version_config.KubeSchedulerVersionConfig"
    ]
    """<p>The Kubernetes scheduler configuration defaults and constraints.</p>"""
    kube_controller_manager_config: NotRequired[
        "capo_eks.types.kube_controller_manager_version_config.KubeControllerManagerVersionConfig"
    ]
    """<p>The Kubernetes controller manager configuration defaults and constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneConfigInfo) -> dict:
    out: dict = {}
    if "kube_api_server_config" in value:
        import capo_eks.types.kube_api_server_version_config

        out["kubeApiServerConfig"] = (
            capo_eks.types.kube_api_server_version_config.serialize_json(
                value["kube_api_server_config"]
            )
        )
    if "kube_scheduler_config" in value:
        import capo_eks.types.kube_scheduler_version_config

        out["kubeSchedulerConfig"] = (
            capo_eks.types.kube_scheduler_version_config.serialize_json(
                value["kube_scheduler_config"]
            )
        )
    if "kube_controller_manager_config" in value:
        import capo_eks.types.kube_controller_manager_version_config

        out["kubeControllerManagerConfig"] = (
            capo_eks.types.kube_controller_manager_version_config.serialize_json(
                value["kube_controller_manager_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlPlaneConfigInfo:
    out: ControlPlaneConfigInfo = {}  # type: ignore[typeddict-item]
    if data.get("kubeApiServerConfig") is not None:
        import capo_eks.types.kube_api_server_version_config

        out["kube_api_server_config"] = (
            capo_eks.types.kube_api_server_version_config.deserialize_json(
                data["kubeApiServerConfig"]
            )
        )
    if data.get("kubeSchedulerConfig") is not None:
        import capo_eks.types.kube_scheduler_version_config

        out["kube_scheduler_config"] = (
            capo_eks.types.kube_scheduler_version_config.deserialize_json(
                data["kubeSchedulerConfig"]
            )
        )
    if data.get("kubeControllerManagerConfig") is not None:
        import capo_eks.types.kube_controller_manager_version_config

        out["kube_controller_manager_config"] = (
            capo_eks.types.kube_controller_manager_version_config.deserialize_json(
                data["kubeControllerManagerConfig"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.eks#KubeControllerManagerVersionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.horizontal_pod_autoscaler_controller_version_config
    import capo_eks.types.pod_gc_controller_version_config


class KubeControllerManagerVersionConfig(TypedDict, closed=True):
    pod_gc_controller_config: NotRequired[
        "capo_eks.types.pod_gc_controller_version_config.PodGcControllerVersionConfig"
    ]
    """<p>The pod garbage collection controller configuration with default value and constraints.</p>"""
    horizontal_pod_autoscaler_controller_config: NotRequired[
        "capo_eks.types.horizontal_pod_autoscaler_controller_version_config.HorizontalPodAutoscalerControllerVersionConfig"
    ]
    """<p>The horizontal pod autoscaler controller configuration with default value and constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubeControllerManagerVersionConfig) -> dict:
    out: dict = {}
    if "pod_gc_controller_config" in value:
        import capo_eks.types.pod_gc_controller_version_config

        out["podGcControllerConfig"] = (
            capo_eks.types.pod_gc_controller_version_config.serialize_json(
                value["pod_gc_controller_config"]
            )
        )
    if "horizontal_pod_autoscaler_controller_config" in value:
        import capo_eks.types.horizontal_pod_autoscaler_controller_version_config

        out["horizontalPodAutoscalerControllerConfig"] = (
            capo_eks.types.horizontal_pod_autoscaler_controller_version_config.serialize_json(
                value["horizontal_pod_autoscaler_controller_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubeControllerManagerVersionConfig:
    out: KubeControllerManagerVersionConfig = {}  # type: ignore[typeddict-item]
    if data.get("podGcControllerConfig") is not None:
        import capo_eks.types.pod_gc_controller_version_config

        out["pod_gc_controller_config"] = (
            capo_eks.types.pod_gc_controller_version_config.deserialize_json(
                data["podGcControllerConfig"]
            )
        )
    if data.get("horizontalPodAutoscalerControllerConfig") is not None:
        import capo_eks.types.horizontal_pod_autoscaler_controller_version_config

        out["horizontal_pod_autoscaler_controller_config"] = (
            capo_eks.types.horizontal_pod_autoscaler_controller_version_config.deserialize_json(
                data["horizontalPodAutoscalerControllerConfig"]
            )
        )
    return out

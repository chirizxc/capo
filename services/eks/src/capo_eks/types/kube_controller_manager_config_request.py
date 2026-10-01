"""Generated from Smithy shape ``com.amazonaws.eks#KubeControllerManagerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.horizontal_pod_autoscaler_controller_config_request
    import capo_eks.types.pod_gc_controller_config_request


class KubeControllerManagerConfigRequest(TypedDict, closed=True):
    pod_gc_controller_config: NotRequired[
        "capo_eks.types.pod_gc_controller_config_request.PodGcControllerConfigRequest"
    ]
    """<p>The pod garbage collection controller configuration.</p>"""
    horizontal_pod_autoscaler_controller_config: NotRequired[
        "capo_eks.types.horizontal_pod_autoscaler_controller_config_request.HorizontalPodAutoscalerControllerConfigRequest"
    ]
    """<p>The horizontal pod autoscaler controller configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubeControllerManagerConfigRequest) -> dict:
    out: dict = {}
    if "pod_gc_controller_config" in value:
        import capo_eks.types.pod_gc_controller_config_request

        out["podGcControllerConfig"] = (
            capo_eks.types.pod_gc_controller_config_request.serialize_json(
                value["pod_gc_controller_config"]
            )
        )
    if "horizontal_pod_autoscaler_controller_config" in value:
        import capo_eks.types.horizontal_pod_autoscaler_controller_config_request

        out["horizontalPodAutoscalerControllerConfig"] = (
            capo_eks.types.horizontal_pod_autoscaler_controller_config_request.serialize_json(
                value["horizontal_pod_autoscaler_controller_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubeControllerManagerConfigRequest:
    out: KubeControllerManagerConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("podGcControllerConfig") is not None:
        import capo_eks.types.pod_gc_controller_config_request

        out["pod_gc_controller_config"] = (
            capo_eks.types.pod_gc_controller_config_request.deserialize_json(
                data["podGcControllerConfig"]
            )
        )
    if data.get("horizontalPodAutoscalerControllerConfig") is not None:
        import capo_eks.types.horizontal_pod_autoscaler_controller_config_request

        out["horizontal_pod_autoscaler_controller_config"] = (
            capo_eks.types.horizontal_pod_autoscaler_controller_config_request.deserialize_json(
                data["horizontalPodAutoscalerControllerConfig"]
            )
        )
    return out

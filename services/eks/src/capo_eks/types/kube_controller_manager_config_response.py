"""Generated from Smithy shape ``com.amazonaws.eks#KubeControllerManagerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.horizontal_pod_autoscaler_controller_config_response
    import capo_eks.types.pod_gc_controller_config_response


class KubeControllerManagerConfigResponse(TypedDict, closed=True):
    pod_gc_controller_config: NotRequired[
        "capo_eks.types.pod_gc_controller_config_response.PodGcControllerConfigResponse"
    ]
    """<p>The pod garbage collection controller configuration.</p>"""
    horizontal_pod_autoscaler_controller_config: NotRequired[
        "capo_eks.types.horizontal_pod_autoscaler_controller_config_response.HorizontalPodAutoscalerControllerConfigResponse"
    ]
    """<p>The horizontal pod autoscaler controller configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubeControllerManagerConfigResponse) -> dict:
    out: dict = {}
    if "pod_gc_controller_config" in value:
        import capo_eks.types.pod_gc_controller_config_response

        out["podGcControllerConfig"] = (
            capo_eks.types.pod_gc_controller_config_response.serialize_json(
                value["pod_gc_controller_config"]
            )
        )
    if "horizontal_pod_autoscaler_controller_config" in value:
        import capo_eks.types.horizontal_pod_autoscaler_controller_config_response

        out["horizontalPodAutoscalerControllerConfig"] = (
            capo_eks.types.horizontal_pod_autoscaler_controller_config_response.serialize_json(
                value["horizontal_pod_autoscaler_controller_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubeControllerManagerConfigResponse:
    out: KubeControllerManagerConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("podGcControllerConfig") is not None:
        import capo_eks.types.pod_gc_controller_config_response

        out["pod_gc_controller_config"] = (
            capo_eks.types.pod_gc_controller_config_response.deserialize_json(
                data["podGcControllerConfig"]
            )
        )
    if data.get("horizontalPodAutoscalerControllerConfig") is not None:
        import capo_eks.types.horizontal_pod_autoscaler_controller_config_response

        out["horizontal_pod_autoscaler_controller_config"] = (
            capo_eks.types.horizontal_pod_autoscaler_controller_config_response.deserialize_json(
                data["horizontalPodAutoscalerControllerConfig"]
            )
        )
    return out

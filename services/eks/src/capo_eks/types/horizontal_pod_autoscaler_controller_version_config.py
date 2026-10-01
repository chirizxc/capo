"""Generated from Smithy shape ``com.amazonaws.eks#HorizontalPodAutoscalerControllerVersionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.duration_parameter_config


class HorizontalPodAutoscalerControllerVersionConfig(TypedDict, closed=True):
    horizontal_pod_autoscaler_sync_period: NotRequired[
        "capo_eks.types.duration_parameter_config.DurationParameterConfig"
    ]
    """<p>The HPA sync period configuration with default value and constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HorizontalPodAutoscalerControllerVersionConfig) -> dict:
    out: dict = {}
    if "horizontal_pod_autoscaler_sync_period" in value:
        import capo_eks.types.duration_parameter_config

        out["horizontalPodAutoscalerSyncPeriod"] = (
            capo_eks.types.duration_parameter_config.serialize_json(
                value["horizontal_pod_autoscaler_sync_period"]
            )
        )
    return out


def deserialize_json(data: dict) -> HorizontalPodAutoscalerControllerVersionConfig:
    out: HorizontalPodAutoscalerControllerVersionConfig = {}  # type: ignore[typeddict-item]
    if data.get("horizontalPodAutoscalerSyncPeriod") is not None:
        import capo_eks.types.duration_parameter_config

        out["horizontal_pod_autoscaler_sync_period"] = (
            capo_eks.types.duration_parameter_config.deserialize_json(
                data["horizontalPodAutoscalerSyncPeriod"]
            )
        )
    return out

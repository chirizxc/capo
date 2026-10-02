"""Generated from Smithy shape ``com.amazonaws.eks#HorizontalPodAutoscalerControllerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class HorizontalPodAutoscalerControllerConfigResponse(TypedDict, closed=True):
    horizontal_pod_autoscaler_sync_period: NotRequired["capo_eks.types.string.String"]
    """<p>The interval between each sync of the horizontal pod autoscaler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HorizontalPodAutoscalerControllerConfigResponse) -> dict:
    out: dict = {}
    if "horizontal_pod_autoscaler_sync_period" in value:
        out["horizontalPodAutoscalerSyncPeriod"] = value[
            "horizontal_pod_autoscaler_sync_period"
        ]
    return out


def deserialize_json(data: dict) -> HorizontalPodAutoscalerControllerConfigResponse:
    out: HorizontalPodAutoscalerControllerConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("horizontalPodAutoscalerSyncPeriod") is not None:
        out["horizontal_pod_autoscaler_sync_period"] = data[
            "horizontalPodAutoscalerSyncPeriod"
        ]
    return out

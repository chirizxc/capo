"""Generated from Smithy shape ``com.amazonaws.eks#HorizontalPodAutoscalerControllerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class HorizontalPodAutoscalerControllerConfigRequest(TypedDict, closed=True):
    horizontal_pod_autoscaler_sync_period: NotRequired["capo_eks.types.string.String"]
    """<p>The interval between each sync of the horizontal pod autoscaler. Valid values are single-unit durations such as <code>15s</code> or <code>1m</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HorizontalPodAutoscalerControllerConfigRequest) -> dict:
    out: dict = {}
    if "horizontal_pod_autoscaler_sync_period" in value:
        out["horizontalPodAutoscalerSyncPeriod"] = value[
            "horizontal_pod_autoscaler_sync_period"
        ]
    return out


def deserialize_json(data: dict) -> HorizontalPodAutoscalerControllerConfigRequest:
    out: HorizontalPodAutoscalerControllerConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("horizontalPodAutoscalerSyncPeriod") is not None:
        out["horizontal_pod_autoscaler_sync_period"] = data[
            "horizontalPodAutoscalerSyncPeriod"
        ]
    return out

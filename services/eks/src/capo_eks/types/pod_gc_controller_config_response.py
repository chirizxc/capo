"""Generated from Smithy shape ``com.amazonaws.eks#PodGcControllerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.terminated_pod_gc_threshold_value


class PodGcControllerConfigResponse(TypedDict, closed=True):
    terminated_pod_gc_threshold: NotRequired[
        "capo_eks.types.terminated_pod_gc_threshold_value.TerminatedPodGcThresholdValue"
    ]
    """<p>The number of terminated pods that can exist before the garbage collector starts deleting them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PodGcControllerConfigResponse) -> dict:
    out: dict = {}
    if "terminated_pod_gc_threshold" in value:
        out["terminatedPodGcThreshold"] = value["terminated_pod_gc_threshold"]
    return out


def deserialize_json(data: dict) -> PodGcControllerConfigResponse:
    out: PodGcControllerConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("terminatedPodGcThreshold") is not None:
        out["terminated_pod_gc_threshold"] = data["terminatedPodGcThreshold"]
    return out

"""Generated from Smithy shape ``com.amazonaws.eks#PodGcControllerVersionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.integer_parameter_config


class PodGcControllerVersionConfig(TypedDict, closed=True):
    terminated_pod_gc_threshold: NotRequired[
        "capo_eks.types.integer_parameter_config.IntegerParameterConfig"
    ]
    """<p>The terminated pod garbage collection threshold configuration with default value and constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PodGcControllerVersionConfig) -> dict:
    out: dict = {}
    if "terminated_pod_gc_threshold" in value:
        import capo_eks.types.integer_parameter_config

        out["terminatedPodGcThreshold"] = (
            capo_eks.types.integer_parameter_config.serialize_json(
                value["terminated_pod_gc_threshold"]
            )
        )
    return out


def deserialize_json(data: dict) -> PodGcControllerVersionConfig:
    out: PodGcControllerVersionConfig = {}  # type: ignore[typeddict-item]
    if data.get("terminatedPodGcThreshold") is not None:
        import capo_eks.types.integer_parameter_config

        out["terminated_pod_gc_threshold"] = (
            capo_eks.types.integer_parameter_config.deserialize_json(
                data["terminatedPodGcThreshold"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.eks#ControlPlaneScalingTierInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_integer
    import capo_eks.types.control_plane_config_info
    import capo_eks.types.string


class ControlPlaneScalingTierInfo(TypedDict, closed=True):
    tier_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the scaling tier.</p>"""
    api_request_concurrency: NotRequired["capo_eks.types.boxed_integer.BoxedInteger"]
    """<p>The maximum API request concurrency supported by this tier.</p>"""
    pod_scheduling_rate_per_second: NotRequired[
        "capo_eks.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum pod scheduling rate per second supported by this tier.</p>"""
    cluster_database_size_gb: NotRequired["capo_eks.types.boxed_integer.BoxedInteger"]
    """<p>The maximum cluster database size in GB supported by this tier.</p>"""
    control_plane_component_config_overrides: NotRequired[
        "capo_eks.types.control_plane_config_info.ControlPlaneConfigInfo"
    ]
    """<p>The control plane component configuration overrides specific to this scaling tier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneScalingTierInfo) -> dict:
    out: dict = {}
    if "tier_name" in value:
        out["tierName"] = value["tier_name"]
    if "api_request_concurrency" in value:
        out["apiRequestConcurrency"] = value["api_request_concurrency"]
    if "pod_scheduling_rate_per_second" in value:
        out["podSchedulingRatePerSecond"] = value["pod_scheduling_rate_per_second"]
    if "cluster_database_size_gb" in value:
        out["clusterDatabaseSizeGb"] = value["cluster_database_size_gb"]
    if "control_plane_component_config_overrides" in value:
        import capo_eks.types.control_plane_config_info

        out["controlPlaneComponentConfigOverrides"] = (
            capo_eks.types.control_plane_config_info.serialize_json(
                value["control_plane_component_config_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlPlaneScalingTierInfo:
    out: ControlPlaneScalingTierInfo = {}  # type: ignore[typeddict-item]
    if data.get("tierName") is not None:
        out["tier_name"] = data["tierName"]
    if data.get("apiRequestConcurrency") is not None:
        out["api_request_concurrency"] = data["apiRequestConcurrency"]
    if data.get("podSchedulingRatePerSecond") is not None:
        out["pod_scheduling_rate_per_second"] = data["podSchedulingRatePerSecond"]
    if data.get("clusterDatabaseSizeGb") is not None:
        out["cluster_database_size_gb"] = data["clusterDatabaseSizeGb"]
    if data.get("controlPlaneComponentConfigOverrides") is not None:
        import capo_eks.types.control_plane_config_info

        out["control_plane_component_config_overrides"] = (
            capo_eks.types.control_plane_config_info.deserialize_json(
                data["controlPlaneComponentConfigOverrides"]
            )
        )
    return out

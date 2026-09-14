"""Generated from Smithy shape ``com.amazonaws.medialive#MonitorDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_min1_max2048
    import capo_medialive.types.signal_map_monitor_deployment_status


class MonitorDeployment(TypedDict, closed=True):
    details_uri: NotRequired[
        "capo_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """URI associated with a signal map's monitor deployment."""
    error_message: NotRequired[
        "capo_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """Error message associated with a failed monitor deployment of a signal map."""
    status: NotRequired[
        "capo_medialive.types.signal_map_monitor_deployment_status.SignalMapMonitorDeploymentStatus"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorDeployment) -> dict:
    out: dict = {}
    if "details_uri" in value:
        out["detailsUri"] = value["details_uri"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "status" in value:
        import capo_medialive.types.signal_map_monitor_deployment_status

        out["status"] = (
            capo_medialive.types.signal_map_monitor_deployment_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> MonitorDeployment:
    out: MonitorDeployment = {}  # type: ignore[typeddict-item]
    if data.get("detailsUri") is not None:
        out["details_uri"] = data["detailsUri"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("status") is not None:
        import capo_medialive.types.signal_map_monitor_deployment_status

        out["status"] = (
            capo_medialive.types.signal_map_monitor_deployment_status.deserialize_json(
                data["status"]
            )
        )
    return out

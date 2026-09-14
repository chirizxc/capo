"""Generated from Smithy shape ``com.amazonaws.costexplorer#NetworkResourceUtilization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class NetworkResourceUtilization(TypedDict, closed=True):
    network_in_bytes_per_second: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The network inbound throughput utilization measured in Bytes per second (Bps). </p>"""
    network_out_bytes_per_second: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The network outbound throughput utilization measured in Bytes per second (Bps). </p>"""
    network_packets_in_per_second: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The network inbound packets that are measured in packets per second. </p>"""
    network_packets_out_per_second: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The network outbound packets that are measured in packets per second. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkResourceUtilization) -> dict:
    out: dict = {}
    if "network_in_bytes_per_second" in value:
        out["NetworkInBytesPerSecond"] = value["network_in_bytes_per_second"]
    if "network_out_bytes_per_second" in value:
        out["NetworkOutBytesPerSecond"] = value["network_out_bytes_per_second"]
    if "network_packets_in_per_second" in value:
        out["NetworkPacketsInPerSecond"] = value["network_packets_in_per_second"]
    if "network_packets_out_per_second" in value:
        out["NetworkPacketsOutPerSecond"] = value["network_packets_out_per_second"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkResourceUtilization:
    out: NetworkResourceUtilization = {}  # type: ignore[typeddict-item]
    if data.get("NetworkInBytesPerSecond") is not None:
        out["network_in_bytes_per_second"] = data["NetworkInBytesPerSecond"]
    if data.get("NetworkOutBytesPerSecond") is not None:
        out["network_out_bytes_per_second"] = data["NetworkOutBytesPerSecond"]
    if data.get("NetworkPacketsInPerSecond") is not None:
        out["network_packets_in_per_second"] = data["NetworkPacketsInPerSecond"]
    if data.get("NetworkPacketsOutPerSecond") is not None:
        out["network_packets_out_per_second"] = data["NetworkPacketsOutPerSecond"]
    return out

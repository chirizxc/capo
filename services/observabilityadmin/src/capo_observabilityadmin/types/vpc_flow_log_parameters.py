"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#VPCFlowLogParameters``."""

from typing_extensions import NotRequired, TypedDict


class VPCFlowLogParameters(TypedDict, closed=True):
    log_format: NotRequired["str"]
    """<p> The format in which VPC Flow Log entries should be logged. </p>"""
    traffic_type: NotRequired["str"]
    """<p> The type of traffic to log (ACCEPT, REJECT, or ALL). </p>"""
    max_aggregation_interval: NotRequired["int"]
    """<p> The maximum interval in seconds between the capture of flow log records. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCFlowLogParameters) -> dict:
    out: dict = {}
    if "log_format" in value:
        out["LogFormat"] = value["log_format"]
    if "traffic_type" in value:
        out["TrafficType"] = value["traffic_type"]
    if "max_aggregation_interval" in value:
        out["MaxAggregationInterval"] = value["max_aggregation_interval"]
    return out


def deserialize_json(data: dict) -> VPCFlowLogParameters:
    out: VPCFlowLogParameters = {}  # type: ignore[typeddict-item]
    if data.get("LogFormat") is not None:
        out["log_format"] = data["LogFormat"]
    if data.get("TrafficType") is not None:
        out["traffic_type"] = data["TrafficType"]
    if data.get("MaxAggregationInterval") is not None:
        out["max_aggregation_interval"] = data["MaxAggregationInterval"]
    return out

"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RistRouterInputConfiguration``."""

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError


class RistRouterInputConfiguration(TypedDict, closed=True):
    port: "int"
    """<p>The port number used for the RIST protocol in the router input configuration.</p>"""
    recovery_latency_milliseconds: "int"
    """<p>The recovery latency in milliseconds for the RIST protocol in the router input configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RistRouterInputConfiguration) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    out["recoveryLatencyMilliseconds"] = value["recovery_latency_milliseconds"]
    return out


def deserialize_json(data: dict) -> RistRouterInputConfiguration:
    out: RistRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        raise DeserializationError("RistRouterInputConfiguration.port required")
    if data.get("recoveryLatencyMilliseconds") is not None:
        out["recovery_latency_milliseconds"] = data["recoveryLatencyMilliseconds"]
    else:
        raise DeserializationError(
            "RistRouterInputConfiguration.recovery_latency_milliseconds required"
        )
    return out

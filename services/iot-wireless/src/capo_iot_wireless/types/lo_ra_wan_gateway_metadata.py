"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANGatewayMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.double
    import capo_iot_wireless.types.gateway_eui


class LoRaWANGatewayMetadata(TypedDict, closed=True):
    gateway_eui: NotRequired["capo_iot_wireless.types.gateway_eui.GatewayEui"]
    """<p>The gateway's EUI value.</p>"""
    snr: NotRequired["capo_iot_wireless.types.double.Double"]
    """<p>The SNR value.</p>"""
    rssi: NotRequired["capo_iot_wireless.types.double.Double"]
    """<p>The RSSI value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANGatewayMetadata) -> dict:
    out: dict = {}
    if "gateway_eui" in value:
        out["GatewayEui"] = value["gateway_eui"]
    if "snr" in value:
        out["Snr"] = (
            "NaN"
            if value["snr"] != value["snr"]
            else "Infinity"
            if value["snr"] == float("inf")
            else "-Infinity"
            if value["snr"] == float("-inf")
            else value["snr"]
        )
    if "rssi" in value:
        out["Rssi"] = (
            "NaN"
            if value["rssi"] != value["rssi"]
            else "Infinity"
            if value["rssi"] == float("inf")
            else "-Infinity"
            if value["rssi"] == float("-inf")
            else value["rssi"]
        )
    return out


def deserialize_json(data: dict) -> LoRaWANGatewayMetadata:
    out: LoRaWANGatewayMetadata = {}  # type: ignore[typeddict-item]
    if data.get("GatewayEui") is not None:
        out["gateway_eui"] = data["GatewayEui"]
    if data.get("Snr") is not None:
        out["snr"] = float(data["Snr"])
    if data.get("Rssi") is not None:
        out["rssi"] = float(data["Rssi"])
    return out

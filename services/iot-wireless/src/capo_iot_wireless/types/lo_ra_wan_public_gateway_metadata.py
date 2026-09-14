"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANPublicGatewayMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.dl_allowed
    import capo_iot_wireless.types.double
    import capo_iot_wireless.types.id
    import capo_iot_wireless.types.provider_net_id
    import capo_iot_wireless.types.rf_region


class LoRaWANPublicGatewayMetadata(TypedDict, closed=True):
    provider_net_id: NotRequired[
        "capo_iot_wireless.types.provider_net_id.ProviderNetId"
    ]
    """<p>The ID of the LoRaWAN public network provider.</p>"""
    id: NotRequired["capo_iot_wireless.types.id.Id"]
    """<p>The ID of the gateways that are operated by the network provider.</p>"""
    rssi: NotRequired["capo_iot_wireless.types.double.Double"]
    """<p>The RSSI (received signal strength indicator) value.</p>"""
    snr: NotRequired["capo_iot_wireless.types.double.Double"]
    """<p>The SNR (signal to noise ratio) value.</p>"""
    rf_region: NotRequired["capo_iot_wireless.types.rf_region.RfRegion"]
    dl_allowed: NotRequired["capo_iot_wireless.types.dl_allowed.DlAllowed"]
    """<p>Boolean that indicates whether downlink is allowed using the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANPublicGatewayMetadata) -> dict:
    out: dict = {}
    if "provider_net_id" in value:
        out["ProviderNetId"] = value["provider_net_id"]
    if "id" in value:
        out["Id"] = value["id"]
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
    if "rf_region" in value:
        out["RfRegion"] = value["rf_region"]
    if "dl_allowed" in value:
        out["DlAllowed"] = value["dl_allowed"]
    return out


def deserialize_json(data: dict) -> LoRaWANPublicGatewayMetadata:
    out: LoRaWANPublicGatewayMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ProviderNetId") is not None:
        out["provider_net_id"] = data["ProviderNetId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Rssi") is not None:
        out["rssi"] = float(data["Rssi"])
    if data.get("Snr") is not None:
        out["snr"] = float(data["Snr"])
    if data.get("RfRegion") is not None:
        out["rf_region"] = data["RfRegion"]
    if data.get("DlAllowed") is not None:
        out["dl_allowed"] = data["DlAllowed"]
    return out

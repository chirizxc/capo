"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANDeviceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.dev_eui
    import capo_iot_wireless.types.integer
    import capo_iot_wireless.types.iso_date_time_string
    import capo_iot_wireless.types.lo_ra_wan_gateway_metadata_list
    import capo_iot_wireless.types.lo_ra_wan_public_gateway_metadata_list


class LoRaWANDeviceMetadata(TypedDict, closed=True):
    dev_eui: NotRequired["capo_iot_wireless.types.dev_eui.DevEui"]
    """<p>The DevEUI value.</p>"""
    f_port: NotRequired["capo_iot_wireless.types.integer.Integer"]
    """<p>The FPort value.</p>"""
    data_rate: NotRequired["capo_iot_wireless.types.integer.Integer"]
    """<p>The DataRate value.</p>"""
    frequency: NotRequired["capo_iot_wireless.types.integer.Integer"]
    """<p>The device's channel frequency in Hz.</p>"""
    timestamp: NotRequired[
        "capo_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time of the metadata.</p>"""
    gateways: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_gateway_metadata_list.LoRaWANGatewayMetadataList"
    ]
    """<p>Information about the gateways accessed by the device.</p>"""
    public_gateways: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_public_gateway_metadata_list.LoRaWANPublicGatewayMetadataList"
    ]
    """<p>Information about the LoRaWAN public network accessed by the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANDeviceMetadata) -> dict:
    out: dict = {}
    if "dev_eui" in value:
        out["DevEui"] = value["dev_eui"]
    if "f_port" in value:
        out["FPort"] = value["f_port"]
    if "data_rate" in value:
        out["DataRate"] = value["data_rate"]
    if "frequency" in value:
        out["Frequency"] = value["frequency"]
    if "timestamp" in value:
        out["Timestamp"] = value["timestamp"]
    if "gateways" in value:
        import capo_iot_wireless.types.lo_ra_wan_gateway_metadata_list

        out["Gateways"] = (
            capo_iot_wireless.types.lo_ra_wan_gateway_metadata_list.serialize_json(
                value["gateways"]
            )
        )
    if "public_gateways" in value:
        import capo_iot_wireless.types.lo_ra_wan_public_gateway_metadata_list

        out["PublicGateways"] = (
            capo_iot_wireless.types.lo_ra_wan_public_gateway_metadata_list.serialize_json(
                value["public_gateways"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANDeviceMetadata:
    out: LoRaWANDeviceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("DevEui") is not None:
        out["dev_eui"] = data["DevEui"]
    if data.get("FPort") is not None:
        out["f_port"] = data["FPort"]
    if data.get("DataRate") is not None:
        out["data_rate"] = data["DataRate"]
    if data.get("Frequency") is not None:
        out["frequency"] = data["Frequency"]
    if data.get("Timestamp") is not None:
        out["timestamp"] = data["Timestamp"]
    if data.get("Gateways") is not None:
        import capo_iot_wireless.types.lo_ra_wan_gateway_metadata_list

        out["gateways"] = (
            capo_iot_wireless.types.lo_ra_wan_gateway_metadata_list.deserialize_json(
                data["Gateways"]
            )
        )
    if data.get("PublicGateways") is not None:
        import capo_iot_wireless.types.lo_ra_wan_public_gateway_metadata_list

        out["public_gateways"] = (
            capo_iot_wireless.types.lo_ra_wan_public_gateway_metadata_list.deserialize_json(
                data["PublicGateways"]
            )
        )
    return out

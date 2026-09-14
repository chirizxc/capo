"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.fuota_device_status
    import capo_iot_wireless.types.iso_date_time_string
    import capo_iot_wireless.types.lo_ra_wan_list_device
    import capo_iot_wireless.types.mc_group_id
    import capo_iot_wireless.types.multicast_device_status
    import capo_iot_wireless.types.positioning_config_status
    import capo_iot_wireless.types.sidewalk_list_device
    import capo_iot_wireless.types.wireless_device_arn
    import capo_iot_wireless.types.wireless_device_id
    import capo_iot_wireless.types.wireless_device_name
    import capo_iot_wireless.types.wireless_device_type


class WirelessDeviceStatistics(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.wireless_device_arn.WirelessDeviceArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    id: NotRequired["capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"]
    """<p>The ID of the wireless device reporting the data.</p>"""
    type: NotRequired["capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"]
    """<p>The wireless device type.</p>"""
    name: NotRequired["capo_iot_wireless.types.wireless_device_name.WirelessDeviceName"]
    """<p>The name of the resource.</p>"""
    destination_name: NotRequired[
        "capo_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination to which the device is assigned.</p>"""
    last_uplink_received_at: NotRequired[
        "capo_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time when the most recent uplink was received.</p> <note> <p>Theis value is only valid for 3 months.</p> </note>"""
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_list_device.LoRaWANListDevice"
    ]
    """<p>LoRaWAN device info.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_list_device.SidewalkListDevice"
    ]
    """<p>The Sidewalk account credentials.</p>"""
    fuota_device_status: NotRequired[
        "capo_iot_wireless.types.fuota_device_status.FuotaDeviceStatus"
    ]
    multicast_device_status: NotRequired[
        "capo_iot_wireless.types.multicast_device_status.MulticastDeviceStatus"
    ]
    """<p>The status of the wireless device in the multicast group.</p>"""
    mc_group_id: NotRequired["capo_iot_wireless.types.mc_group_id.McGroupId"]
    positioning: NotRequired[
        "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for LoRaWAN and Amazon Sidewalk enabled devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceStatistics) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_iot_wireless.types.wireless_device_type

        out["Type"] = capo_iot_wireless.types.wireless_device_type.serialize_json(
            value["type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "last_uplink_received_at" in value:
        out["LastUplinkReceivedAt"] = value["last_uplink_received_at"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_list_device

        out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_list_device.serialize_json(
            value["lo_ra_wan"]
        )
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_list_device

        out["Sidewalk"] = capo_iot_wireless.types.sidewalk_list_device.serialize_json(
            value["sidewalk"]
        )
    if "fuota_device_status" in value:
        import capo_iot_wireless.types.fuota_device_status

        out["FuotaDeviceStatus"] = (
            capo_iot_wireless.types.fuota_device_status.serialize_json(
                value["fuota_device_status"]
            )
        )
    if "multicast_device_status" in value:
        out["MulticastDeviceStatus"] = value["multicast_device_status"]
    if "mc_group_id" in value:
        out["McGroupId"] = value["mc_group_id"]
    if "positioning" in value:
        import capo_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            capo_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> WirelessDeviceStatistics:
    out: WirelessDeviceStatistics = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_iot_wireless.types.wireless_device_type

        out["type"] = capo_iot_wireless.types.wireless_device_type.deserialize_json(
            data["Type"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DestinationName") is not None:
        out["destination_name"] = data["DestinationName"]
    if data.get("LastUplinkReceivedAt") is not None:
        out["last_uplink_received_at"] = data["LastUplinkReceivedAt"]
    if data.get("LoRaWAN") is not None:
        import capo_iot_wireless.types.lo_ra_wan_list_device

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_list_device.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if data.get("Sidewalk") is not None:
        import capo_iot_wireless.types.sidewalk_list_device

        out["sidewalk"] = capo_iot_wireless.types.sidewalk_list_device.deserialize_json(
            data["Sidewalk"]
        )
    if data.get("FuotaDeviceStatus") is not None:
        import capo_iot_wireless.types.fuota_device_status

        out["fuota_device_status"] = (
            capo_iot_wireless.types.fuota_device_status.deserialize_json(
                data["FuotaDeviceStatus"]
            )
        )
    if data.get("MulticastDeviceStatus") is not None:
        out["multicast_device_status"] = data["MulticastDeviceStatus"]
    if data.get("McGroupId") is not None:
        out["mc_group_id"] = data["McGroupId"]
    if data.get("Positioning") is not None:
        import capo_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            capo_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    return out

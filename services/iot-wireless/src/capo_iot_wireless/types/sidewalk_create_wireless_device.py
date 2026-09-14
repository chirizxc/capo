"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkCreateWirelessDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.device_profile_id
    import capo_iot_wireless.types.sidewalk_manufacturing_sn
    import capo_iot_wireless.types.sidewalk_positioning


class SidewalkCreateWirelessDevice(TypedDict, closed=True):
    device_profile_id: NotRequired[
        "capo_iot_wireless.types.device_profile_id.DeviceProfileId"
    ]
    """<p>The ID of the Sidewalk device profile.</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.sidewalk_positioning.SidewalkPositioning"
    ]
    """<p>The Positioning object of the Sidewalk device.</p>"""
    sidewalk_manufacturing_sn: NotRequired[
        "capo_iot_wireless.types.sidewalk_manufacturing_sn.SidewalkManufacturingSn"
    ]
    """<p>The Sidewalk manufacturing serial number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkCreateWirelessDevice) -> dict:
    out: dict = {}
    if "device_profile_id" in value:
        out["DeviceProfileId"] = value["device_profile_id"]
    if "positioning" in value:
        import capo_iot_wireless.types.sidewalk_positioning

        out["Positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.serialize_json(
                value["positioning"]
            )
        )
    if "sidewalk_manufacturing_sn" in value:
        out["SidewalkManufacturingSn"] = value["sidewalk_manufacturing_sn"]
    return out


def deserialize_json(data: dict) -> SidewalkCreateWirelessDevice:
    out: SidewalkCreateWirelessDevice = {}  # type: ignore[typeddict-item]
    if data.get("DeviceProfileId") is not None:
        out["device_profile_id"] = data["DeviceProfileId"]
    if data.get("Positioning") is not None:
        import capo_iot_wireless.types.sidewalk_positioning

        out["positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.deserialize_json(
                data["Positioning"]
            )
        )
    if data.get("SidewalkManufacturingSn") is not None:
        out["sidewalk_manufacturing_sn"] = data["SidewalkManufacturingSn"]
    return out

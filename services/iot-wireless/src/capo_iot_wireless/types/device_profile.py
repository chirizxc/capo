"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.device_profile_arn
    import capo_iot_wireless.types.device_profile_id
    import capo_iot_wireless.types.device_profile_name


class DeviceProfile(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.device_profile_arn.DeviceProfileArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired["capo_iot_wireless.types.device_profile_name.DeviceProfileName"]
    """<p>The name of the resource.</p>"""
    id: NotRequired["capo_iot_wireless.types.device_profile_id.DeviceProfileId"]
    """<p>The ID of the device profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceProfile) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeviceProfile:
    out: DeviceProfile = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out

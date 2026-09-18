"""Generated from Smithy shape ``com.amazonaws.iotwireless#ServiceProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.service_profile_arn
    import capo_iot_wireless.types.service_profile_id
    import capo_iot_wireless.types.service_profile_name


class ServiceProfile(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.service_profile_arn.ServiceProfileArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired["capo_iot_wireless.types.service_profile_name.ServiceProfileName"]
    """<p>The name of the resource.</p>"""
    id: NotRequired["capo_iot_wireless.types.service_profile_id.ServiceProfileId"]
    """<p>The ID of the service profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceProfile) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ServiceProfile:
    out: ServiceProfile = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out

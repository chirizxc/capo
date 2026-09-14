"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.destination_arn
    import capo_iot_wireless.types.destination_name


class CreateDestinationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.destination_arn.DestinationArn"]
    """<p>The Amazon Resource Name of the new resource.</p>"""
    name: NotRequired["capo_iot_wireless.types.destination_name.DestinationName"]
    """<p>The name of the new resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDestinationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateDestinationResponse:
    out: CreateDestinationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out

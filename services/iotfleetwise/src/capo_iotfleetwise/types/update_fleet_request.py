"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.fleet_id


class UpdateFleetRequest(TypedDict, closed=True):
    fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of the fleet to update. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> An updated description of the fleet. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateFleetRequest) -> dict:
    out: dict = {}
    out["fleetId"] = value["fleet_id"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateFleetRequest:
    out: UpdateFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("UpdateFleetRequest.fleet_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out

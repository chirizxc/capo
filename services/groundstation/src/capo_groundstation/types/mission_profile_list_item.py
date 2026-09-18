"""Generated from Smithy shape ``com.amazonaws.groundstation#MissionProfileListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.aws_region
    import capo_groundstation.types.mission_profile_arn
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.uuid


class MissionProfileListItem(TypedDict, closed=True):
    mission_profile_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>UUID of a mission profile.</p>"""
    mission_profile_arn: NotRequired[
        "capo_groundstation.types.mission_profile_arn.MissionProfileArn"
    ]
    """<p>ARN of a mission profile.</p>"""
    region: NotRequired["capo_groundstation.types.aws_region.AWSRegion"]
    """<p>Region of a mission profile.</p>"""
    name: NotRequired["capo_groundstation.types.safe_name.SafeName"]
    """<p>Name of a mission profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissionProfileListItem) -> dict:
    out: dict = {}
    if "mission_profile_id" in value:
        out["missionProfileId"] = value["mission_profile_id"]
    if "mission_profile_arn" in value:
        out["missionProfileArn"] = value["mission_profile_arn"]
    if "region" in value:
        out["region"] = value["region"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> MissionProfileListItem:
    out: MissionProfileListItem = {}  # type: ignore[typeddict-item]
    if data.get("missionProfileId") is not None:
        out["mission_profile_id"] = data["missionProfileId"]
    if data.get("missionProfileArn") is not None:
        out["mission_profile_arn"] = data["missionProfileArn"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out

"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.arn
    import capo_route53profiles.types.name
    import capo_route53profiles.types.resource_id
    import capo_route53profiles.types.share_status


class ProfileSummary(TypedDict, closed=True):
    id: NotRequired["capo_route53profiles.types.resource_id.ResourceId"]
    """<p> ID of the Profile. </p>"""
    arn: NotRequired["capo_route53profiles.types.arn.Arn"]
    """<p> The Amazon Resource Name (ARN) of the Profile. </p>"""
    name: NotRequired["capo_route53profiles.types.name.Name"]
    """<p> Name of the Profile. </p>"""
    share_status: NotRequired["capo_route53profiles.types.share_status.ShareStatus"]
    """<p> Share status of the Profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "share_status" in value:
        import capo_route53profiles.types.share_status

        out["ShareStatus"] = capo_route53profiles.types.share_status.serialize_json(
            value["share_status"]
        )
    return out


def deserialize_json(data: dict) -> ProfileSummary:
    out: ProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ShareStatus") is not None:
        import capo_route53profiles.types.share_status

        out["share_status"] = capo_route53profiles.types.share_status.deserialize_json(
            data["ShareStatus"]
        )
    return out

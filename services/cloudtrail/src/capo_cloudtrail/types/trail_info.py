"""Generated from Smithy shape ``com.amazonaws.cloudtrail#TrailInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.string


class TrailInfo(TypedDict, closed=True):
    trail_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>The ARN of a trail.</p>"""
    name: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>The name of a trail.</p>"""
    home_region: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>The Amazon Web Services Region in which a trail was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrailInfo) -> dict:
    out: dict = {}
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrailInfo:
    out: TrailInfo = {}  # type: ignore[typeddict-item]
    if data.get("TrailARN") is not None:
        out["trail_arn"] = data["TrailARN"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("HomeRegion") is not None:
        out["home_region"] = data["HomeRegion"]
    return out

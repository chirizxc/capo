"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#Thing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.thing_arn
    import capo_iotthingsgraph.types.thing_name


class Thing(TypedDict, closed=True):
    thing_arn: NotRequired["capo_iotthingsgraph.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing.</p>"""
    thing_name: NotRequired["capo_iotthingsgraph.types.thing_name.ThingName"]
    """<p>The name of the thing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Thing) -> dict:
    out: dict = {}
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Thing:
    out: Thing = {}  # type: ignore[typeddict-item]
    if data.get("thingArn") is not None:
        out["thing_arn"] = data["thingArn"]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    return out

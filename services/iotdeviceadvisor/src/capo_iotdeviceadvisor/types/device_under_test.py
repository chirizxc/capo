"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#DeviceUnderTest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.amazon_resource_name


class DeviceUnderTest(TypedDict, closed=True):
    thing_arn: NotRequired[
        "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Lists device's thing ARN.</p>"""
    certificate_arn: NotRequired[
        "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Lists device's certificate ARN.</p>"""
    device_role_arn: NotRequired[
        "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Lists device's role ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceUnderTest) -> dict:
    out: dict = {}
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "device_role_arn" in value:
        out["deviceRoleArn"] = value["device_role_arn"]
    return out


def deserialize_json(data: dict) -> DeviceUnderTest:
    out: DeviceUnderTest = {}  # type: ignore[typeddict-item]
    if data.get("thingArn") is not None:
        out["thing_arn"] = data["thingArn"]
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    if data.get("deviceRoleArn") is not None:
        out["device_role_arn"] = data["deviceRoleArn"]
    return out

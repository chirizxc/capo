"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServicePower``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.float
    import capo_lightsail.types.string


class ContainerServicePower(TypedDict, closed=True):
    power_id: NotRequired["capo_lightsail.types.string.string"]
    """<p>The ID of the power (<code>nano-1</code>).</p>"""
    price: NotRequired["capo_lightsail.types.float.float"]
    """<p>The monthly price of the power in USD.</p>"""
    cpu_count: NotRequired["capo_lightsail.types.float.float"]
    """<p>The number of vCPUs included in the power.</p>"""
    ram_size_in_gb: NotRequired["capo_lightsail.types.float.float"]
    """<p>The amount of RAM (in GB) of the power.</p>"""
    name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The friendly name of the power (<code>nano</code>).</p>"""
    is_active: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the power is active and can be specified for container services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServicePower) -> dict:
    out: dict = {}
    if "power_id" in value:
        out["powerId"] = value["power_id"]
    if "price" in value:
        out["price"] = (
            "NaN"
            if value["price"] != value["price"]
            else "Infinity"
            if value["price"] == float("inf")
            else "-Infinity"
            if value["price"] == float("-inf")
            else value["price"]
        )
    if "cpu_count" in value:
        out["cpuCount"] = (
            "NaN"
            if value["cpu_count"] != value["cpu_count"]
            else "Infinity"
            if value["cpu_count"] == float("inf")
            else "-Infinity"
            if value["cpu_count"] == float("-inf")
            else value["cpu_count"]
        )
    if "ram_size_in_gb" in value:
        out["ramSizeInGb"] = (
            "NaN"
            if value["ram_size_in_gb"] != value["ram_size_in_gb"]
            else "Infinity"
            if value["ram_size_in_gb"] == float("inf")
            else "-Infinity"
            if value["ram_size_in_gb"] == float("-inf")
            else value["ram_size_in_gb"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServicePower:
    out: ContainerServicePower = {}  # type: ignore[typeddict-item]
    if data.get("powerId") is not None:
        out["power_id"] = data["powerId"]
    if data.get("price") is not None:
        out["price"] = float(data["price"])
    if data.get("cpuCount") is not None:
        out["cpu_count"] = float(data["cpuCount"])
    if data.get("ramSizeInGb") is not None:
        out["ram_size_in_gb"] = float(data["ramSizeInGb"])
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("isActive") is not None:
        out["is_active"] = data["isActive"]
    return out

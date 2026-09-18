"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#Capacity``."""

from typing_extensions import NotRequired, TypedDict


class Capacity(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the type of capacity, such as memory.</p>"""
    unit: NotRequired["str"]
    """<p>The unit of measure for the type of capacity.</p>"""
    total: NotRequired["int"]
    """<p>The total capacity on the device.</p>"""
    used: NotRequired["int"]
    """<p>The amount of capacity used on the device.</p>"""
    available: NotRequired["int"]
    """<p>The amount of capacity available for use on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Capacity) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "unit" in value:
        out["unit"] = value["unit"]
    if "total" in value:
        out["total"] = value["total"]
    if "used" in value:
        out["used"] = value["used"]
    if "available" in value:
        out["available"] = value["available"]
    return out


def deserialize_json(data: dict) -> Capacity:
    out: Capacity = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    if data.get("total") is not None:
        out["total"] = data["total"]
    if data.get("used") is not None:
        out["used"] = data["used"]
    if data.get("available") is not None:
        out["available"] = data["available"]
    return out

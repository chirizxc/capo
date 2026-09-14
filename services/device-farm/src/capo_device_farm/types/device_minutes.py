"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceMinutes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.double


class DeviceMinutes(TypedDict, closed=True):
    total: NotRequired["capo_device_farm.types.double.Double"]
    """<p>When specified, represents the total minutes used by the resource to run tests.</p>"""
    metered: NotRequired["capo_device_farm.types.double.Double"]
    """<p>When specified, represents only the sum of metered minutes used by the resource to run tests.</p>"""
    unmetered: NotRequired["capo_device_farm.types.double.Double"]
    """<p>When specified, represents only the sum of unmetered minutes used by the resource to run tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceMinutes) -> dict:
    out: dict = {}
    if "total" in value:
        out["total"] = (
            "NaN"
            if value["total"] != value["total"]
            else "Infinity"
            if value["total"] == float("inf")
            else "-Infinity"
            if value["total"] == float("-inf")
            else value["total"]
        )
    if "metered" in value:
        out["metered"] = (
            "NaN"
            if value["metered"] != value["metered"]
            else "Infinity"
            if value["metered"] == float("inf")
            else "-Infinity"
            if value["metered"] == float("-inf")
            else value["metered"]
        )
    if "unmetered" in value:
        out["unmetered"] = (
            "NaN"
            if value["unmetered"] != value["unmetered"]
            else "Infinity"
            if value["unmetered"] == float("inf")
            else "-Infinity"
            if value["unmetered"] == float("-inf")
            else value["unmetered"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceMinutes:
    out: DeviceMinutes = {}  # type: ignore[typeddict-item]
    if data.get("total") is not None:
        out["total"] = float(data["total"])
    if data.get("metered") is not None:
        out["metered"] = float(data["metered"])
    if data.get("unmetered") is not None:
        out["unmetered"] = float(data["unmetered"])
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#DoubleConfigurationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.double


class DoubleConfigurationOptions(TypedDict, closed=True):
    default_value: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The Security Hub CSPM default value for a control parameter that is a double. </p>"""
    min: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The minimum valid value for a control parameter that is a double. </p>"""
    max: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The maximum valid value for a control parameter that is a double. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DoubleConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["DefaultValue"] = (
            "NaN"
            if value["default_value"] != value["default_value"]
            else "Infinity"
            if value["default_value"] == float("inf")
            else "-Infinity"
            if value["default_value"] == float("-inf")
            else value["default_value"]
        )
    if "min" in value:
        out["Min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    if "max" in value:
        out["Max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    return out


def deserialize_json(data: dict) -> DoubleConfigurationOptions:
    out: DoubleConfigurationOptions = {}  # type: ignore[typeddict-item]
    if data.get("DefaultValue") is not None:
        out["default_value"] = float(data["DefaultValue"])
    if data.get("Min") is not None:
        out["min"] = float(data["Min"])
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    return out

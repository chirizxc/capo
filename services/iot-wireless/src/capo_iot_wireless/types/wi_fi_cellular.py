"""Generated from Smithy shape ``com.amazonaws.iotwireless#WiFiCellular``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.confidence_percent


class WiFiCellular(TypedDict, closed=True):
    confidence_percent: "capo_iot_wireless.types.confidence_percent.ConfidencePercent"
    """<p>The confidence level for WiFi and cellular position estimates, expressed as a percentage. This value determines the size of the confidence area or uncertainty radius for the estimated position. A higher confidence level produces a larger uncertainty radius, while a lower confidence level produces a smaller, more precise radius.</p> <p>Valid range: 50 to 99 inclusive. If not specified, the default value of 68 is used, which corresponds to approximately one standard deviation of the normal distribution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WiFiCellular) -> dict:
    out: dict = {}
    out["ConfidencePercent"] = value.get("confidence_percent", 68)
    return out


def deserialize_json(data: dict) -> WiFiCellular:
    out: WiFiCellular = {}  # type: ignore[typeddict-item]
    if data.get("ConfidencePercent") is not None:
        out["confidence_percent"] = data["ConfidencePercent"]
    else:
        out["confidence_percent"] = 68
    return out

"""Generated from Smithy shape ``com.amazonaws.appconfig#VendedMetricsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.boolean


class VendedMetricsSettings(TypedDict, closed=True):
    enabled: NotRequired["capo_appconfig.types.boolean.Boolean"]
    """<p>Specifies whether vended metrics are enabled for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VendedMetricsSettings) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> VendedMetricsSettings:
    out: VendedMetricsSettings = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out

"""Generated from Smithy shape ``com.amazonaws.sesv2#ConfigurationOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.tracking_configuration_overrides


class ConfigurationOverrides(TypedDict, closed=True):
    tracking: NotRequired[
        "capo_sesv2.types.tracking_configuration_overrides.TrackingConfigurationOverrides"
    ]
    """<p>An object that overrides the open and click tracking settings that would otherwise apply to the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationOverrides) -> dict:
    out: dict = {}
    if "tracking" in value:
        import capo_sesv2.types.tracking_configuration_overrides

        out["Tracking"] = (
            capo_sesv2.types.tracking_configuration_overrides.serialize_json(
                value["tracking"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationOverrides:
    out: ConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if data.get("Tracking") is not None:
        import capo_sesv2.types.tracking_configuration_overrides

        out["tracking"] = (
            capo_sesv2.types.tracking_configuration_overrides.deserialize_json(
                data["Tracking"]
            )
        )
    return out

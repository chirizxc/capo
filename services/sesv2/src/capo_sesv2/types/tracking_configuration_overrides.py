"""Generated from Smithy shape ``com.amazonaws.sesv2#TrackingConfigurationOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.feature_status


class TrackingConfigurationOverrides(TypedDict, closed=True):
    open_tracking_enabled: NotRequired["capo_sesv2.types.feature_status.FeatureStatus"]
    """<p>Specifies whether Amazon SES tracks when the recipient opens this message. Can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Amazon SES tracks opens for this message, even when your account-level and configuration set settings don't enable open tracking.</p> </li> <li> <p> <code>DISABLED</code> – Amazon SES doesn't track opens for this message, even when your account-level or configuration set settings enable open tracking. Amazon SES doesn't add the tracking image to the message.</p> </li> </ul> <p>If you don't specify this value, Amazon SES uses the open tracking setting that would otherwise apply to the message.</p>"""
    click_tracking_enabled: NotRequired["capo_sesv2.types.feature_status.FeatureStatus"]
    """<p>Specifies whether Amazon SES tracks when the recipient clicks a link in this message. Can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Amazon SES tracks clicks for this message, even when your account-level and configuration set settings don't enable click tracking.</p> </li> <li> <p> <code>DISABLED</code> – Amazon SES doesn't track clicks for this message, even when your account-level or configuration set settings enable click tracking. Amazon SES doesn't rewrite the links in the message.</p> </li> </ul> <p>If you don't specify this value, Amazon SES uses the click tracking setting that would otherwise apply to the message.</p> <note> <p>Enabling open or click tracking with an override doesn't create an event destination. Amazon SES records the resulting open and click events in VDM, where you can review them using VDM metrics and Message Insights. To also receive these events at a destination that you own, the configuration set that the message uses must have an event destination that publishes open and click events.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingConfigurationOverrides) -> dict:
    out: dict = {}
    if "open_tracking_enabled" in value:
        import capo_sesv2.types.feature_status

        out["OpenTrackingEnabled"] = capo_sesv2.types.feature_status.serialize_json(
            value["open_tracking_enabled"]
        )
    if "click_tracking_enabled" in value:
        import capo_sesv2.types.feature_status

        out["ClickTrackingEnabled"] = capo_sesv2.types.feature_status.serialize_json(
            value["click_tracking_enabled"]
        )
    return out


def deserialize_json(data: dict) -> TrackingConfigurationOverrides:
    out: TrackingConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if data.get("OpenTrackingEnabled") is not None:
        import capo_sesv2.types.feature_status

        out["open_tracking_enabled"] = capo_sesv2.types.feature_status.deserialize_json(
            data["OpenTrackingEnabled"]
        )
    if data.get("ClickTrackingEnabled") is not None:
        import capo_sesv2.types.feature_status

        out["click_tracking_enabled"] = (
            capo_sesv2.types.feature_status.deserialize_json(
                data["ClickTrackingEnabled"]
            )
        )
    return out

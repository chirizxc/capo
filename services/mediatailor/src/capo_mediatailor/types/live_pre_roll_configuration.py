"""Generated from Smithy shape ``com.amazonaws.mediatailor#LivePreRollConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.pre_roll_ad_decision_server_configuration


class LivePreRollConfiguration(TypedDict, closed=True):
    ad_decision_server_url: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.</p>"""
    max_duration_seconds: NotRequired["capo_mediatailor.types.__integer.__integer"]
    """<p>The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.</p>"""
    ad_decision_server_configuration: NotRequired[
        "capo_mediatailor.types.pre_roll_ad_decision_server_configuration.PreRollAdDecisionServerConfiguration"
    ]
    """<p>The configuration for the ad decision server (ADS) for live pre-roll ads. The configuration contains settings that control how MediaTailor processes VAST responses for pre-roll ad breaks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LivePreRollConfiguration) -> dict:
    out: dict = {}
    if "ad_decision_server_url" in value:
        out["AdDecisionServerUrl"] = value["ad_decision_server_url"]
    if "max_duration_seconds" in value:
        out["MaxDurationSeconds"] = value["max_duration_seconds"]
    if "ad_decision_server_configuration" in value:
        import capo_mediatailor.types.pre_roll_ad_decision_server_configuration

        out["AdDecisionServerConfiguration"] = (
            capo_mediatailor.types.pre_roll_ad_decision_server_configuration.serialize_json(
                value["ad_decision_server_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> LivePreRollConfiguration:
    out: LivePreRollConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AdDecisionServerUrl") is not None:
        out["ad_decision_server_url"] = data["AdDecisionServerUrl"]
    if data.get("MaxDurationSeconds") is not None:
        out["max_duration_seconds"] = data["MaxDurationSeconds"]
    if data.get("AdDecisionServerConfiguration") is not None:
        import capo_mediatailor.types.pre_roll_ad_decision_server_configuration

        out["ad_decision_server_configuration"] = (
            capo_mediatailor.types.pre_roll_ad_decision_server_configuration.deserialize_json(
                data["AdDecisionServerConfiguration"]
            )
        )
    return out

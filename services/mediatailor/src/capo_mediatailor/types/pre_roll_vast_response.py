"""Generated from Smithy shape ``com.amazonaws.mediatailor#PreRollVastResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.pre_roll_ad_sequencing_mode


class PreRollVastResponse(TypedDict, closed=True):
    ad_sequencing_mode: NotRequired[
        "capo_mediatailor.types.pre_roll_ad_sequencing_mode.PreRollAdSequencingMode"
    ]
    """<p>The ad sequencing mode for live pre-roll ads. <code>FOLLOW_AD_SEQUENCE</code> inserts sequenced ads in increasing order and uses standalone ads only as replacements when a sequenced ad fails. <code>IGNORE_AD_SEQUENCE</code> inserts ads in the order they appear in the VAST response, regardless of sequence attributes. The default behavior is <code>IGNORE_AD_SEQUENCE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreRollVastResponse) -> dict:
    out: dict = {}
    if "ad_sequencing_mode" in value:
        import capo_mediatailor.types.pre_roll_ad_sequencing_mode

        out["AdSequencingMode"] = (
            capo_mediatailor.types.pre_roll_ad_sequencing_mode.serialize_json(
                value["ad_sequencing_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> PreRollVastResponse:
    out: PreRollVastResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdSequencingMode") is not None:
        import capo_mediatailor.types.pre_roll_ad_sequencing_mode

        out["ad_sequencing_mode"] = (
            capo_mediatailor.types.pre_roll_ad_sequencing_mode.deserialize_json(
                data["AdSequencingMode"]
            )
        )
    return out

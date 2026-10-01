"""Generated from Smithy shape ``com.amazonaws.mediatailor#VastResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.ad_sequencing_mode


class VastResponse(TypedDict, closed=True):
    ad_sequencing_mode: NotRequired[
        "capo_mediatailor.types.ad_sequencing_mode.AdSequencingMode"
    ]
    """<p>The ad sequencing mode that controls how MediaTailor handles sequenced and standalone ads in VAST responses. <code>FOLLOW_AD_SEQUENCE</code> inserts sequenced ads in increasing order for both live and VOD workflows, using standalone ads only as replacements when a sequenced ad fails. <code>FOLLOW_AD_SEQUENCE_ONLY_LIVE</code> enables ad sequencing for live workflows only. <code>FOLLOW_AD_SEQUENCE_ONLY_VOD</code> enables ad sequencing for VOD workflows only. <code>IGNORE_AD_SEQUENCE</code> inserts ads in the order they appear in the VAST response, regardless of sequence attributes. The default behavior is <code>IGNORE_AD_SEQUENCE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VastResponse) -> dict:
    out: dict = {}
    if "ad_sequencing_mode" in value:
        import capo_mediatailor.types.ad_sequencing_mode

        out["AdSequencingMode"] = (
            capo_mediatailor.types.ad_sequencing_mode.serialize_json(
                value["ad_sequencing_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> VastResponse:
    out: VastResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdSequencingMode") is not None:
        import capo_mediatailor.types.ad_sequencing_mode

        out["ad_sequencing_mode"] = (
            capo_mediatailor.types.ad_sequencing_mode.deserialize_json(
                data["AdSequencingMode"]
            )
        )
    return out

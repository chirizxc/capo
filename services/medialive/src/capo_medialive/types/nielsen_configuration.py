"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.nielsen_pcm_to_id3_tagging_state


class NielsenConfiguration(TypedDict, closed=True):
    distributor_id: NotRequired["capo_medialive.types.__string.__string"]
    """Enter the Distributor ID assigned to your organization by Nielsen."""
    nielsen_pcm_to_id3_tagging: NotRequired[
        "capo_medialive.types.nielsen_pcm_to_id3_tagging_state.NielsenPcmToId3TaggingState"
    ]
    """Enables Nielsen PCM to ID3 tagging"""


# --- restJson1 ser/de ---
def serialize_json(value: NielsenConfiguration) -> dict:
    out: dict = {}
    if "distributor_id" in value:
        out["distributorId"] = value["distributor_id"]
    if "nielsen_pcm_to_id3_tagging" in value:
        import capo_medialive.types.nielsen_pcm_to_id3_tagging_state

        out["nielsenPcmToId3Tagging"] = (
            capo_medialive.types.nielsen_pcm_to_id3_tagging_state.serialize_json(
                value["nielsen_pcm_to_id3_tagging"]
            )
        )
    return out


def deserialize_json(data: dict) -> NielsenConfiguration:
    out: NielsenConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("distributorId") is not None:
        out["distributor_id"] = data["distributorId"]
    if data.get("nielsenPcmToId3Tagging") is not None:
        import capo_medialive.types.nielsen_pcm_to_id3_tagging_state

        out["nielsen_pcm_to_id3_tagging"] = (
            capo_medialive.types.nielsen_pcm_to_id3_tagging_state.deserialize_json(
                data["nielsenPcmToId3Tagging"]
            )
        )
    return out

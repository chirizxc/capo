"""Generated from Smithy shape ``com.amazonaws.medialive#CmafIngestWatermarkingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.cmaf_ingest_ab_watermarker_irdeto_settings


class CmafIngestWatermarkingSettings(TypedDict, closed=True):
    cmaf_ingest_ab_watermarker_irdeto_settings: NotRequired[
        "capo_medialive.types.cmaf_ingest_ab_watermarker_irdeto_settings.CmafIngestAbWatermarkerIrdetoSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CmafIngestWatermarkingSettings) -> dict:
    out: dict = {}
    if "cmaf_ingest_ab_watermarker_irdeto_settings" in value:
        import capo_medialive.types.cmaf_ingest_ab_watermarker_irdeto_settings

        out["cmafIngestAbWatermarkerIrdetoSettings"] = (
            capo_medialive.types.cmaf_ingest_ab_watermarker_irdeto_settings.serialize_json(
                value["cmaf_ingest_ab_watermarker_irdeto_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CmafIngestWatermarkingSettings:
    out: CmafIngestWatermarkingSettings = {}  # type: ignore[typeddict-item]
    if data.get("cmafIngestAbWatermarkerIrdetoSettings") is not None:
        import capo_medialive.types.cmaf_ingest_ab_watermarker_irdeto_settings

        out["cmaf_ingest_ab_watermarker_irdeto_settings"] = (
            capo_medialive.types.cmaf_ingest_ab_watermarker_irdeto_settings.deserialize_json(
                data["cmafIngestAbWatermarkerIrdetoSettings"]
            )
        )
    return out

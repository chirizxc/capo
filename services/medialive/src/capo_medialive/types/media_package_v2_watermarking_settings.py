"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageV2WatermarkingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.media_package_v2_ab_watermarker_irdeto_settings


class MediaPackageV2WatermarkingSettings(TypedDict, closed=True):
    media_package_v2_ab_watermarker_irdeto_settings: NotRequired[
        "capo_medialive.types.media_package_v2_ab_watermarker_irdeto_settings.MediaPackageV2AbWatermarkerIrdetoSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageV2WatermarkingSettings) -> dict:
    out: dict = {}
    if "media_package_v2_ab_watermarker_irdeto_settings" in value:
        import capo_medialive.types.media_package_v2_ab_watermarker_irdeto_settings

        out["mediaPackageV2AbWatermarkerIrdetoSettings"] = (
            capo_medialive.types.media_package_v2_ab_watermarker_irdeto_settings.serialize_json(
                value["media_package_v2_ab_watermarker_irdeto_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaPackageV2WatermarkingSettings:
    out: MediaPackageV2WatermarkingSettings = {}  # type: ignore[typeddict-item]
    if data.get("mediaPackageV2AbWatermarkerIrdetoSettings") is not None:
        import capo_medialive.types.media_package_v2_ab_watermarker_irdeto_settings

        out["media_package_v2_ab_watermarker_irdeto_settings"] = (
            capo_medialive.types.media_package_v2_ab_watermarker_irdeto_settings.deserialize_json(
                data["mediaPackageV2AbWatermarkerIrdetoSettings"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionSelectorSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.ancillary_source_settings
    import capo_medialive.types.arib_source_settings
    import capo_medialive.types.dvb_sub_source_settings
    import capo_medialive.types.embedded_source_settings
    import capo_medialive.types.scte20_source_settings
    import capo_medialive.types.scte27_source_settings
    import capo_medialive.types.smart_subtitle_source_settings
    import capo_medialive.types.teletext_source_settings


class CaptionSelectorSettings(TypedDict, closed=True):
    ancillary_source_settings: NotRequired[
        "capo_medialive.types.ancillary_source_settings.AncillarySourceSettings"
    ]
    arib_source_settings: NotRequired[
        "capo_medialive.types.arib_source_settings.AribSourceSettings"
    ]
    dvb_sub_source_settings: NotRequired[
        "capo_medialive.types.dvb_sub_source_settings.DvbSubSourceSettings"
    ]
    embedded_source_settings: NotRequired[
        "capo_medialive.types.embedded_source_settings.EmbeddedSourceSettings"
    ]
    scte20_source_settings: NotRequired[
        "capo_medialive.types.scte20_source_settings.Scte20SourceSettings"
    ]
    scte27_source_settings: NotRequired[
        "capo_medialive.types.scte27_source_settings.Scte27SourceSettings"
    ]
    teletext_source_settings: NotRequired[
        "capo_medialive.types.teletext_source_settings.TeletextSourceSettings"
    ]
    smart_subtitle_source_settings: NotRequired[
        "capo_medialive.types.smart_subtitle_source_settings.SmartSubtitleSourceSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSelectorSettings) -> dict:
    out: dict = {}
    if "ancillary_source_settings" in value:
        import capo_medialive.types.ancillary_source_settings

        out["ancillarySourceSettings"] = (
            capo_medialive.types.ancillary_source_settings.serialize_json(
                value["ancillary_source_settings"]
            )
        )
    if "arib_source_settings" in value:
        import capo_medialive.types.arib_source_settings

        out["aribSourceSettings"] = (
            capo_medialive.types.arib_source_settings.serialize_json(
                value["arib_source_settings"]
            )
        )
    if "dvb_sub_source_settings" in value:
        import capo_medialive.types.dvb_sub_source_settings

        out["dvbSubSourceSettings"] = (
            capo_medialive.types.dvb_sub_source_settings.serialize_json(
                value["dvb_sub_source_settings"]
            )
        )
    if "embedded_source_settings" in value:
        import capo_medialive.types.embedded_source_settings

        out["embeddedSourceSettings"] = (
            capo_medialive.types.embedded_source_settings.serialize_json(
                value["embedded_source_settings"]
            )
        )
    if "scte20_source_settings" in value:
        import capo_medialive.types.scte20_source_settings

        out["scte20SourceSettings"] = (
            capo_medialive.types.scte20_source_settings.serialize_json(
                value["scte20_source_settings"]
            )
        )
    if "scte27_source_settings" in value:
        import capo_medialive.types.scte27_source_settings

        out["scte27SourceSettings"] = (
            capo_medialive.types.scte27_source_settings.serialize_json(
                value["scte27_source_settings"]
            )
        )
    if "teletext_source_settings" in value:
        import capo_medialive.types.teletext_source_settings

        out["teletextSourceSettings"] = (
            capo_medialive.types.teletext_source_settings.serialize_json(
                value["teletext_source_settings"]
            )
        )
    if "smart_subtitle_source_settings" in value:
        import capo_medialive.types.smart_subtitle_source_settings

        out["smartSubtitleSourceSettings"] = (
            capo_medialive.types.smart_subtitle_source_settings.serialize_json(
                value["smart_subtitle_source_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CaptionSelectorSettings:
    out: CaptionSelectorSettings = {}  # type: ignore[typeddict-item]
    if data.get("ancillarySourceSettings") is not None:
        import capo_medialive.types.ancillary_source_settings

        out["ancillary_source_settings"] = (
            capo_medialive.types.ancillary_source_settings.deserialize_json(
                data["ancillarySourceSettings"]
            )
        )
    if data.get("aribSourceSettings") is not None:
        import capo_medialive.types.arib_source_settings

        out["arib_source_settings"] = (
            capo_medialive.types.arib_source_settings.deserialize_json(
                data["aribSourceSettings"]
            )
        )
    if data.get("dvbSubSourceSettings") is not None:
        import capo_medialive.types.dvb_sub_source_settings

        out["dvb_sub_source_settings"] = (
            capo_medialive.types.dvb_sub_source_settings.deserialize_json(
                data["dvbSubSourceSettings"]
            )
        )
    if data.get("embeddedSourceSettings") is not None:
        import capo_medialive.types.embedded_source_settings

        out["embedded_source_settings"] = (
            capo_medialive.types.embedded_source_settings.deserialize_json(
                data["embeddedSourceSettings"]
            )
        )
    if data.get("scte20SourceSettings") is not None:
        import capo_medialive.types.scte20_source_settings

        out["scte20_source_settings"] = (
            capo_medialive.types.scte20_source_settings.deserialize_json(
                data["scte20SourceSettings"]
            )
        )
    if data.get("scte27SourceSettings") is not None:
        import capo_medialive.types.scte27_source_settings

        out["scte27_source_settings"] = (
            capo_medialive.types.scte27_source_settings.deserialize_json(
                data["scte27SourceSettings"]
            )
        )
    if data.get("teletextSourceSettings") is not None:
        import capo_medialive.types.teletext_source_settings

        out["teletext_source_settings"] = (
            capo_medialive.types.teletext_source_settings.deserialize_json(
                data["teletextSourceSettings"]
            )
        )
    if data.get("smartSubtitleSourceSettings") is not None:
        import capo_medialive.types.smart_subtitle_source_settings

        out["smart_subtitle_source_settings"] = (
            capo_medialive.types.smart_subtitle_source_settings.deserialize_json(
                data["smartSubtitleSourceSettings"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#ArchiveGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.archive_cdn_settings
    import capo_medialive.types.output_location_ref


class ArchiveGroupSettings(TypedDict, closed=True):
    archive_cdn_settings: NotRequired[
        "capo_medialive.types.archive_cdn_settings.ArchiveCdnSettings"
    ]
    """Parameters that control interactions with the CDN."""
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """A directory and base filename where archive files should be written."""
    rollover_interval: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """Number of seconds to write to archive file before closing and starting a new one."""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveGroupSettings) -> dict:
    out: dict = {}
    if "archive_cdn_settings" in value:
        import capo_medialive.types.archive_cdn_settings

        out["archiveCdnSettings"] = (
            capo_medialive.types.archive_cdn_settings.serialize_json(
                value["archive_cdn_settings"]
            )
        )
    if "destination" in value:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "rollover_interval" in value:
        out["rolloverInterval"] = value["rollover_interval"]
    return out


def deserialize_json(data: dict) -> ArchiveGroupSettings:
    out: ArchiveGroupSettings = {}  # type: ignore[typeddict-item]
    if data.get("archiveCdnSettings") is not None:
        import capo_medialive.types.archive_cdn_settings

        out["archive_cdn_settings"] = (
            capo_medialive.types.archive_cdn_settings.deserialize_json(
                data["archiveCdnSettings"]
            )
        )
    if data.get("destination") is not None:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.deserialize_json(
            data["destination"]
        )
    if data.get("rolloverInterval") is not None:
        out["rollover_interval"] = data["rolloverInterval"]
    return out

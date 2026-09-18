"""Generated from Smithy shape ``com.amazonaws.medialive#ArchiveOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.archive_container_settings


class ArchiveOutputSettings(TypedDict, closed=True):
    container_settings: NotRequired[
        "capo_medialive.types.archive_container_settings.ArchiveContainerSettings"
    ]
    """Container for this output. Can be auto-detected from extension field."""
    extension: NotRequired["capo_medialive.types.__string.__string"]
    """Output file extension. If excluded, this will be auto-selected from the container type."""
    name_modifier: NotRequired["capo_medialive.types.__string.__string"]
    """String concatenated to the end of the destination filename. Required for multiple outputs of the same type."""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveOutputSettings) -> dict:
    out: dict = {}
    if "container_settings" in value:
        import capo_medialive.types.archive_container_settings

        out["containerSettings"] = (
            capo_medialive.types.archive_container_settings.serialize_json(
                value["container_settings"]
            )
        )
    if "extension" in value:
        out["extension"] = value["extension"]
    if "name_modifier" in value:
        out["nameModifier"] = value["name_modifier"]
    return out


def deserialize_json(data: dict) -> ArchiveOutputSettings:
    out: ArchiveOutputSettings = {}  # type: ignore[typeddict-item]
    if data.get("containerSettings") is not None:
        import capo_medialive.types.archive_container_settings

        out["container_settings"] = (
            capo_medialive.types.archive_container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    if data.get("extension") is not None:
        out["extension"] = data["extension"]
    if data.get("nameModifier") is not None:
        out["name_modifier"] = data["nameModifier"]
    return out

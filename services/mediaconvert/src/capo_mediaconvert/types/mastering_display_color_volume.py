"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MasteringDisplayColorVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.__long


class MasteringDisplayColorVolume(TypedDict, closed=True):
    blue_primary_x: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Blue primary chromaticity x coordinate, in units of 0.00002."""
    blue_primary_y: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Blue primary chromaticity y coordinate, in units of 0.00002."""
    green_primary_x: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Green primary chromaticity x coordinate, in units of 0.00002."""
    green_primary_y: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Green primary chromaticity y coordinate, in units of 0.00002."""
    max_luminance: NotRequired["capo_mediaconvert.types.__long.__long"]
    """Maximum display mastering luminance, in units of 0.0001 cd/m²."""
    min_luminance: NotRequired["capo_mediaconvert.types.__long.__long"]
    """Minimum display mastering luminance, in units of 0.0001 cd/m²."""
    red_primary_x: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Red primary chromaticity x coordinate, in units of 0.00002."""
    red_primary_y: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Red primary chromaticity y coordinate, in units of 0.00002."""
    white_point_x: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """White point chromaticity x coordinate, in units of 0.00002."""
    white_point_y: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """White point chromaticity y coordinate, in units of 0.00002."""


# --- restJson1 ser/de ---
def serialize_json(value: MasteringDisplayColorVolume) -> dict:
    out: dict = {}
    if "blue_primary_x" in value:
        out["bluePrimaryX"] = value["blue_primary_x"]
    if "blue_primary_y" in value:
        out["bluePrimaryY"] = value["blue_primary_y"]
    if "green_primary_x" in value:
        out["greenPrimaryX"] = value["green_primary_x"]
    if "green_primary_y" in value:
        out["greenPrimaryY"] = value["green_primary_y"]
    if "max_luminance" in value:
        out["maxLuminance"] = value["max_luminance"]
    if "min_luminance" in value:
        out["minLuminance"] = value["min_luminance"]
    if "red_primary_x" in value:
        out["redPrimaryX"] = value["red_primary_x"]
    if "red_primary_y" in value:
        out["redPrimaryY"] = value["red_primary_y"]
    if "white_point_x" in value:
        out["whitePointX"] = value["white_point_x"]
    if "white_point_y" in value:
        out["whitePointY"] = value["white_point_y"]
    return out


def deserialize_json(data: dict) -> MasteringDisplayColorVolume:
    out: MasteringDisplayColorVolume = {}  # type: ignore[typeddict-item]
    if data.get("bluePrimaryX") is not None:
        out["blue_primary_x"] = data["bluePrimaryX"]
    if data.get("bluePrimaryY") is not None:
        out["blue_primary_y"] = data["bluePrimaryY"]
    if data.get("greenPrimaryX") is not None:
        out["green_primary_x"] = data["greenPrimaryX"]
    if data.get("greenPrimaryY") is not None:
        out["green_primary_y"] = data["greenPrimaryY"]
    if data.get("maxLuminance") is not None:
        out["max_luminance"] = data["maxLuminance"]
    if data.get("minLuminance") is not None:
        out["min_luminance"] = data["minLuminance"]
    if data.get("redPrimaryX") is not None:
        out["red_primary_x"] = data["redPrimaryX"]
    if data.get("redPrimaryY") is not None:
        out["red_primary_y"] = data["redPrimaryY"]
    if data.get("whitePointX") is not None:
        out["white_point_x"] = data["whitePointX"]
    if data.get("whitePointY") is not None:
        out["white_point_y"] = data["whitePointY"]
    return out

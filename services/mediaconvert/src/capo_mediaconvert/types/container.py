"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Container``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double
    import capo_mediaconvert.types.__list_of_track
    import capo_mediaconvert.types.__long
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.format


class Container(TypedDict, closed=True):
    bit_rate: NotRequired["capo_mediaconvert.types.__long.__long"]
    """The overall bit rate of your media file, in bits per second. This is derived from the file size and duration as (file size in bytes * 8) / duration in seconds."""
    duration: NotRequired["capo_mediaconvert.types.__double.__double"]
    """The total duration of your media file, in seconds."""
    format: NotRequired["capo_mediaconvert.types.format.Format"]
    """The format of your media file. For example: MP4, QuickTime (MOV), Matroska (MKV), WebM, MXF, Wave, AVI, MPEG-TS, MPEG-PS, MP3, FLAC, ASF (Windows Media / WMA), OGG, 3GP, 3G2, AAC (raw ADTS), AC-3, or Enhanced AC-3 (E-AC-3). Note that this will be blank if your media file has a format that the MediaConvert Probe operation does not recognize."""
    start_timecode: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The start timecode of the media file, in HH:MM:SS:FF format (or HH:MM:SS;FF for drop frame timecode). Note that this field is null when the container does not include an embedded start timecode."""
    tracks: NotRequired["capo_mediaconvert.types.__list_of_track.__listOfTrack"]
    """Details about each track (video, audio, or data) in the media file."""


# --- restJson1 ser/de ---
def serialize_json(value: Container) -> dict:
    out: dict = {}
    if "bit_rate" in value:
        out["bitRate"] = value["bit_rate"]
    if "duration" in value:
        out["duration"] = (
            "NaN"
            if value["duration"] != value["duration"]
            else "Infinity"
            if value["duration"] == float("inf")
            else "-Infinity"
            if value["duration"] == float("-inf")
            else value["duration"]
        )
    if "format" in value:
        import capo_mediaconvert.types.format

        out["format"] = capo_mediaconvert.types.format.serialize_json(value["format"])
    if "start_timecode" in value:
        out["startTimecode"] = value["start_timecode"]
    if "tracks" in value:
        import capo_mediaconvert.types.__list_of_track

        out["tracks"] = capo_mediaconvert.types.__list_of_track.serialize_json(
            value["tracks"]
        )
    return out


def deserialize_json(data: dict) -> Container:
    out: Container = {}  # type: ignore[typeddict-item]
    if data.get("bitRate") is not None:
        out["bit_rate"] = data["bitRate"]
    if data.get("duration") is not None:
        out["duration"] = float(data["duration"])
    if data.get("format") is not None:
        import capo_mediaconvert.types.format

        out["format"] = capo_mediaconvert.types.format.deserialize_json(data["format"])
    if data.get("startTimecode") is not None:
        out["start_timecode"] = data["startTimecode"]
    if data.get("tracks") is not None:
        import capo_mediaconvert.types.__list_of_track

        out["tracks"] = capo_mediaconvert.types.__list_of_track.deserialize_json(
            data["tracks"]
        )
    return out

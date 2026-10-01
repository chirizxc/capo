"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PassthroughSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max100
    import capo_mediaconvert.types.frame_control
    import capo_mediaconvert.types.passthrough_segmentation_mode
    import capo_mediaconvert.types.video_selector_mode


class PassthroughSettings(TypedDict, closed=True):
    frame_control: NotRequired["capo_mediaconvert.types.frame_control.FrameControl"]
    """Choose how MediaConvert handles start and end times for input clipping with video passthrough. Your input video codec must be H.264 or H.265 to use IFRAME. To clip at the nearest IDR-frame: Choose Nearest IDR. If an IDR-frame is not found at the frame that you specify, MediaConvert uses the next compatible IDR-frame. Note that your output may be shorter than your input clip duration. To clip at the nearest I-frame: Choose Nearest I-frame. If an I-frame is not found at the frame that you specify, MediaConvert uses the next compatible I-frame. Note that your output may be shorter than your input clip duration. We only recommend this setting for special workflows, and when you choose this setting your output may not be compatible with most players."""
    gops_per_segment: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max100.__integerMin1Max100"
    ]
    """Specify how many input GOPs MediaConvert places in each output segment when you set Passthrough segmentation mode to GOP count. For example, if your input has a closed GOP every 1.92 seconds and you specify 2, each output segment is 3.84 seconds. In this mode, output segment duration is determined by your input GOP structure rather than by your configured Segment length or Fragment length, so segment durations are consistent only when your input GOP cadence is constant. Segments at input discontinuities or ad avails may contain fewer GOPs."""
    segmentation_mode: NotRequired[
        "capo_mediaconvert.types.passthrough_segmentation_mode.PassthroughSegmentationMode"
    ]
    """Choose how MediaConvert determines segment boundaries when you passthrough video to a segmented ABR output (HLS, DASH, or CMAF). This setting applies only to ABR outputs. Keep the default value, Auto, to let MediaConvert choose based on your input: when your input is a segmented HLS or DASH source, MediaConvert reproduces your input's own segment boundaries, with one output segment per input segment; for all other inputs, MediaConvert places boundaries by duration, cutting at the first eligible IDR-frame at or after each configured Segment length or Fragment length target. Choose Duration based to always place boundaries by duration, at the first eligible IDR-frame at or after each configured Segment length or Fragment length target, regardless of your input. When your input GOP duration does not evenly divide your target segment length, output segment durations will vary. Choose GOP count to place a fixed number of input GOPs in every segment, and specify GOPs per segment. Every segment contains the same number of input GOPs, which produces consistent segment durations when your input GOP cadence is constant. In this mode MediaConvert ignores your configured Segment length and Fragment length for video boundary placement. Ad avails and input discontinuities are still honored as segment boundaries."""
    video_selector_mode: NotRequired[
        "capo_mediaconvert.types.video_selector_mode.VideoSelectorMode"
    ]
    """AUTO will select the highest bitrate input in the video selector source. REMUX_ALL will passthrough all the selected streams in the video selector source. When selecting streams from multiple renditions (i.e. using Stream video selector type): REMUX_ALL will only remux all streams selected, and AUTO will use the highest bitrate video stream among the selected streams as source."""


# --- restJson1 ser/de ---
def serialize_json(value: PassthroughSettings) -> dict:
    out: dict = {}
    if "frame_control" in value:
        import capo_mediaconvert.types.frame_control

        out["frameControl"] = capo_mediaconvert.types.frame_control.serialize_json(
            value["frame_control"]
        )
    if "gops_per_segment" in value:
        out["gopsPerSegment"] = value["gops_per_segment"]
    if "segmentation_mode" in value:
        import capo_mediaconvert.types.passthrough_segmentation_mode

        out["segmentationMode"] = (
            capo_mediaconvert.types.passthrough_segmentation_mode.serialize_json(
                value["segmentation_mode"]
            )
        )
    if "video_selector_mode" in value:
        import capo_mediaconvert.types.video_selector_mode

        out["videoSelectorMode"] = (
            capo_mediaconvert.types.video_selector_mode.serialize_json(
                value["video_selector_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> PassthroughSettings:
    out: PassthroughSettings = {}  # type: ignore[typeddict-item]
    if data.get("frameControl") is not None:
        import capo_mediaconvert.types.frame_control

        out["frame_control"] = capo_mediaconvert.types.frame_control.deserialize_json(
            data["frameControl"]
        )
    if data.get("gopsPerSegment") is not None:
        out["gops_per_segment"] = data["gopsPerSegment"]
    if data.get("segmentationMode") is not None:
        import capo_mediaconvert.types.passthrough_segmentation_mode

        out["segmentation_mode"] = (
            capo_mediaconvert.types.passthrough_segmentation_mode.deserialize_json(
                data["segmentationMode"]
            )
        )
    if data.get("videoSelectorMode") is not None:
        import capo_mediaconvert.types.video_selector_mode

        out["video_selector_mode"] = (
            capo_mediaconvert.types.video_selector_mode.deserialize_json(
                data["videoSelectorMode"]
            )
        )
    return out

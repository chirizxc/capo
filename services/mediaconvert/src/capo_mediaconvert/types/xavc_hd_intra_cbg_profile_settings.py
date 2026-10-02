"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdIntraCbgProfileSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.xavc_hd_intra_cbg_profile_class
    import capo_mediaconvert.types.xavc_interlace_mode


class XavcHdIntraCbgProfileSettings(TypedDict, closed=True):
    interlace_mode: NotRequired[
        "capo_mediaconvert.types.xavc_interlace_mode.XavcInterlaceMode"
    ]
    """Choose the scan line type for the output. Keep the default value, Progressive, to create a progressive output, regardless of the scan type of your input. To create an interlaced output, choose Top field first or Follow, default top. Outputs that you create with this profile are always top field first when they are interlaced. When you create an interlaced output, set your output frame rate to 25 or 29.97."""
    xavc_class: NotRequired[
        "capo_mediaconvert.types.xavc_hd_intra_cbg_profile_class.XavcHdIntraCbgProfileClass"
    ]
    """Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""


# --- restJson1 ser/de ---
def serialize_json(value: XavcHdIntraCbgProfileSettings) -> dict:
    out: dict = {}
    if "interlace_mode" in value:
        import capo_mediaconvert.types.xavc_interlace_mode

        out["interlaceMode"] = (
            capo_mediaconvert.types.xavc_interlace_mode.serialize_json(
                value["interlace_mode"]
            )
        )
    if "xavc_class" in value:
        import capo_mediaconvert.types.xavc_hd_intra_cbg_profile_class

        out["xavcClass"] = (
            capo_mediaconvert.types.xavc_hd_intra_cbg_profile_class.serialize_json(
                value["xavc_class"]
            )
        )
    return out


def deserialize_json(data: dict) -> XavcHdIntraCbgProfileSettings:
    out: XavcHdIntraCbgProfileSettings = {}  # type: ignore[typeddict-item]
    if data.get("interlaceMode") is not None:
        import capo_mediaconvert.types.xavc_interlace_mode

        out["interlace_mode"] = (
            capo_mediaconvert.types.xavc_interlace_mode.deserialize_json(
                data["interlaceMode"]
            )
        )
    if data.get("xavcClass") is not None:
        import capo_mediaconvert.types.xavc_hd_intra_cbg_profile_class

        out["xavc_class"] = (
            capo_mediaconvert.types.xavc_hd_intra_cbg_profile_class.deserialize_json(
                data["xavcClass"]
            )
        )
    return out

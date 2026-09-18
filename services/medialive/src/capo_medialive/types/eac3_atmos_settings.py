"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3AtmosSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.__integer_min1_max31
    import capo_medialive.types.eac3_atmos_coding_mode
    import capo_medialive.types.eac3_atmos_drc_line
    import capo_medialive.types.eac3_atmos_drc_rf


class Eac3AtmosSettings(TypedDict, closed=True):
    bitrate: NotRequired["capo_medialive.types.__double.__double"]
    """Average bitrate in bits/second. Valid bitrates depend on the coding mode."""
    coding_mode: NotRequired[
        "capo_medialive.types.eac3_atmos_coding_mode.Eac3AtmosCodingMode"
    ]
    """Dolby Digital Plus with Dolby Atmos coding mode. Determines number of channels."""
    dialnorm: NotRequired[
        "capo_medialive.types.__integer_min1_max31.__integerMin1Max31"
    ]
    """Sets the dialnorm for the output. Default 23."""
    drc_line: NotRequired["capo_medialive.types.eac3_atmos_drc_line.Eac3AtmosDrcLine"]
    """Sets the Dolby dynamic range compression profile."""
    drc_rf: NotRequired["capo_medialive.types.eac3_atmos_drc_rf.Eac3AtmosDrcRf"]
    """Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels."""
    height_trim: NotRequired["capo_medialive.types.__double.__double"]
    """Height dimensional trim. Sets the maximum amount to attenuate the height channels when the downstream player isn??t configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels."""
    surround_trim: NotRequired["capo_medialive.types.__double.__double"]
    """Surround dimensional trim. Sets the maximum amount to attenuate the surround channels when the downstream player isn't configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels."""


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosSettings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = (
            "NaN"
            if value["bitrate"] != value["bitrate"]
            else "Infinity"
            if value["bitrate"] == float("inf")
            else "-Infinity"
            if value["bitrate"] == float("-inf")
            else value["bitrate"]
        )
    if "coding_mode" in value:
        import capo_medialive.types.eac3_atmos_coding_mode

        out["codingMode"] = capo_medialive.types.eac3_atmos_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "dialnorm" in value:
        out["dialnorm"] = value["dialnorm"]
    if "drc_line" in value:
        import capo_medialive.types.eac3_atmos_drc_line

        out["drcLine"] = capo_medialive.types.eac3_atmos_drc_line.serialize_json(
            value["drc_line"]
        )
    if "drc_rf" in value:
        import capo_medialive.types.eac3_atmos_drc_rf

        out["drcRf"] = capo_medialive.types.eac3_atmos_drc_rf.serialize_json(
            value["drc_rf"]
        )
    if "height_trim" in value:
        out["heightTrim"] = (
            "NaN"
            if value["height_trim"] != value["height_trim"]
            else "Infinity"
            if value["height_trim"] == float("inf")
            else "-Infinity"
            if value["height_trim"] == float("-inf")
            else value["height_trim"]
        )
    if "surround_trim" in value:
        out["surroundTrim"] = (
            "NaN"
            if value["surround_trim"] != value["surround_trim"]
            else "Infinity"
            if value["surround_trim"] == float("inf")
            else "-Infinity"
            if value["surround_trim"] == float("-inf")
            else value["surround_trim"]
        )
    return out


def deserialize_json(data: dict) -> Eac3AtmosSettings:
    out: Eac3AtmosSettings = {}  # type: ignore[typeddict-item]
    if data.get("bitrate") is not None:
        out["bitrate"] = float(data["bitrate"])
    if data.get("codingMode") is not None:
        import capo_medialive.types.eac3_atmos_coding_mode

        out["coding_mode"] = (
            capo_medialive.types.eac3_atmos_coding_mode.deserialize_json(
                data["codingMode"]
            )
        )
    if data.get("dialnorm") is not None:
        out["dialnorm"] = data["dialnorm"]
    if data.get("drcLine") is not None:
        import capo_medialive.types.eac3_atmos_drc_line

        out["drc_line"] = capo_medialive.types.eac3_atmos_drc_line.deserialize_json(
            data["drcLine"]
        )
    if data.get("drcRf") is not None:
        import capo_medialive.types.eac3_atmos_drc_rf

        out["drc_rf"] = capo_medialive.types.eac3_atmos_drc_rf.deserialize_json(
            data["drcRf"]
        )
    if data.get("heightTrim") is not None:
        out["height_trim"] = float(data["heightTrim"])
    if data.get("surroundTrim") is not None:
        out["surround_trim"] = float(data["surroundTrim"])
    return out

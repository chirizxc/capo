"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EncodingParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.encoder_profile


class EncodingParametersRequest(TypedDict, closed=True):
    compression_factor: NotRequired["float"]
    """<p> A value that is used to calculate compression for an output. The bitrate of the output is calculated as follows: Output bitrate = (1 / compressionFactor) * (source bitrate) This property only applies to outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol. Valid values are floating point numbers in the range of 3.0 to 10.0, inclusive.</p>"""
    encoder_profile: NotRequired[
        "capo_mediaconnect.types.encoder_profile.EncoderProfile"
    ]
    """<p> A setting on the encoder that drives compression settings. This property only applies to video media streams associated with outputs that use the ST 2110 JPEG XS protocol, if at least one source on the flow uses the CDI protocol.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncodingParametersRequest) -> dict:
    out: dict = {}
    if "compression_factor" in value:
        out["compressionFactor"] = (
            "NaN"
            if value["compression_factor"] != value["compression_factor"]
            else "Infinity"
            if value["compression_factor"] == float("inf")
            else "-Infinity"
            if value["compression_factor"] == float("-inf")
            else value["compression_factor"]
        )
    if "encoder_profile" in value:
        import capo_mediaconnect.types.encoder_profile

        out["encoderProfile"] = capo_mediaconnect.types.encoder_profile.serialize_json(
            value["encoder_profile"]
        )
    return out


def deserialize_json(data: dict) -> EncodingParametersRequest:
    out: EncodingParametersRequest = {}  # type: ignore[typeddict-item]
    if data.get("compressionFactor") is not None:
        out["compression_factor"] = float(data["compressionFactor"])
    if data.get("encoderProfile") is not None:
        import capo_mediaconnect.types.encoder_profile

        out["encoder_profile"] = (
            capo_mediaconnect.types.encoder_profile.deserialize_json(
                data["encoderProfile"]
            )
        )
    return out

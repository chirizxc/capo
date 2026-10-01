"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DurationControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max500
    import capo_mediaconvert.types.__integer_min0_max2147483647
    import capo_mediaconvert.types.__integer_min1_max2147483647


class DurationControl(TypedDict, closed=True):
    integer_duration_maximum_compression_denominator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Required. Denominator of the maximum allowed compression ratio."""
    integer_duration_maximum_compression_numerator: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Required. Numerator of the maximum allowed compression ratio, defined as overrun divided by target duration. For example, numerator 5 with denominator 100 means max 5% compression. Set to 0 to disable compression entirely (only trim or pad will be used)."""
    integer_duration_trim_threshold_milliseconds: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max500.__integerMin0Max500"
    ]
    """Maximum number of fractional milliseconds past an integer second that qualify for the trim path (frame dropping). Default is 0 (trimming disabled)."""


# --- restJson1 ser/de ---
def serialize_json(value: DurationControl) -> dict:
    out: dict = {}
    if "integer_duration_maximum_compression_denominator" in value:
        out["integerDurationMaximumCompressionDenominator"] = value[
            "integer_duration_maximum_compression_denominator"
        ]
    if "integer_duration_maximum_compression_numerator" in value:
        out["integerDurationMaximumCompressionNumerator"] = value[
            "integer_duration_maximum_compression_numerator"
        ]
    if "integer_duration_trim_threshold_milliseconds" in value:
        out["integerDurationTrimThresholdMilliseconds"] = value[
            "integer_duration_trim_threshold_milliseconds"
        ]
    return out


def deserialize_json(data: dict) -> DurationControl:
    out: DurationControl = {}  # type: ignore[typeddict-item]
    if data.get("integerDurationMaximumCompressionDenominator") is not None:
        out["integer_duration_maximum_compression_denominator"] = data[
            "integerDurationMaximumCompressionDenominator"
        ]
    if data.get("integerDurationMaximumCompressionNumerator") is not None:
        out["integer_duration_maximum_compression_numerator"] = data[
            "integerDurationMaximumCompressionNumerator"
        ]
    if data.get("integerDurationTrimThresholdMilliseconds") is not None:
        out["integer_duration_trim_threshold_milliseconds"] = data[
            "integerDurationTrimThresholdMilliseconds"
        ]
    return out

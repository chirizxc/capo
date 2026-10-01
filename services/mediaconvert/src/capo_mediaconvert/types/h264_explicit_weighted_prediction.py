"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264ExplicitWeightedPrediction``."""

from typing import Literal, TypeAlias, cast

"""Enable or disable explicit weighted prediction for the H.264 encoder. Weighted prediction improves compression efficiency for content with fading or brightness changes between frames."""
H264ExplicitWeightedPrediction: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264ExplicitWeightedPrediction) -> str:
    return value


def deserialize_json(data: str) -> H264ExplicitWeightedPrediction:
    return cast(H264ExplicitWeightedPrediction, data)

"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterContentQualityAnalysisType``."""

from typing import Literal, TypeAlias, cast

RouterContentQualityAnalysisType: TypeAlias = Literal["CONTENT_LEVEL",]


# --- restJson1 ser/de ---
def serialize_json(value: RouterContentQualityAnalysisType) -> str:
    return value


def deserialize_json(data: str) -> RouterContentQualityAnalysisType:
    return cast(RouterContentQualityAnalysisType, data)

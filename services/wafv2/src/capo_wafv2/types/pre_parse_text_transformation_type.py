"""Generated from Smithy shape ``com.amazonaws.wafv2#PreParseTextTransformationType``."""

from typing import Literal, TypeAlias, cast

PreParseTextTransformationType: TypeAlias = Literal[
    "NONE",
    "URL_DECODE",
    "URL_DECODE_UNI",
    "COMBINE_DUPLICATE_QUERY_ARGS_BY_COMMA",
    "REPLACE_SEMICOLONS_WITH_AMPERSANDS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreParseTextTransformationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreParseTextTransformationType:
    return cast(PreParseTextTransformationType, data)

"""Generated from Smithy shape ``com.amazonaws.wafv2#PreParseTextTransformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.pre_parse_text_transformation

PreParseTextTransformations: TypeAlias = list[
    "capo_wafv2.types.pre_parse_text_transformation.PreParseTextTransformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreParseTextTransformations) -> list:
    import capo_wafv2.types.pre_parse_text_transformation

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.pre_parse_text_transformation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PreParseTextTransformations:
    import capo_wafv2.types.pre_parse_text_transformation

    out: PreParseTextTransformations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wafv2.types.pre_parse_text_transformation.deserialize_aws_json_1_1(
                item
            )
        )
    return out

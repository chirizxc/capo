"""Generated from Smithy shape ``com.amazonaws.wafv2#MonetizationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.monetization_filter

MonetizationFilterList: TypeAlias = list[
    "capo_wafv2.types.monetization_filter.MonetizationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonetizationFilterList) -> list:
    import capo_wafv2.types.monetization_filter

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.monetization_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MonetizationFilterList:
    import capo_wafv2.types.monetization_filter

    out: MonetizationFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wafv2.types.monetization_filter.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.wafv2#MonetizationFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.monetization_filter_value

MonetizationFilterValueList: TypeAlias = list[
    "capo_wafv2.types.monetization_filter_value.MonetizationFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonetizationFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MonetizationFilterValueList:
    return [item for item in data if item is not None]

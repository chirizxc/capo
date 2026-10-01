"""Generated from Smithy shape ``com.amazonaws.wafv2#RevenuePathStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.revenue_path_statistics

RevenuePathStatisticsList: TypeAlias = list[
    "capo_wafv2.types.revenue_path_statistics.RevenuePathStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevenuePathStatisticsList) -> list:
    import capo_wafv2.types.revenue_path_statistics

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.revenue_path_statistics.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RevenuePathStatisticsList:
    import capo_wafv2.types.revenue_path_statistics

    out: RevenuePathStatisticsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wafv2.types.revenue_path_statistics.deserialize_aws_json_1_1(item)
        )
    return out

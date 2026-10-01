"""Generated from Smithy shape ``com.amazonaws.wafv2#SourceStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.source_statistics

SourceStatisticsList: TypeAlias = list[
    "capo_wafv2.types.source_statistics.SourceStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceStatisticsList) -> list:
    import capo_wafv2.types.source_statistics

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.source_statistics.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SourceStatisticsList:
    import capo_wafv2.types.source_statistics

    out: SourceStatisticsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wafv2.types.source_statistics.deserialize_aws_json_1_1(item))
    return out

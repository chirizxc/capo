"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IndexCategories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.index_category

IndexCategories: TypeAlias = list[
    "capo_cloudwatch_logs.types.index_category.IndexCategory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexCategories) -> list:
    import capo_cloudwatch_logs.types.index_category

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.index_category.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IndexCategories:
    import capo_cloudwatch_logs.types.index_category

    out: IndexCategories = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.index_category.deserialize_aws_json_1_1(item)
        )
    return out

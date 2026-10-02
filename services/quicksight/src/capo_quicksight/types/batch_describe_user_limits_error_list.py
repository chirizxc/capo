"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDescribeUserLimitsErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.batch_describe_user_limits_error

BatchDescribeUserLimitsErrorList: TypeAlias = list[
    "capo_quicksight.types.batch_describe_user_limits_error.BatchDescribeUserLimitsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeUserLimitsErrorList) -> list:
    import capo_quicksight.types.batch_describe_user_limits_error

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.batch_describe_user_limits_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchDescribeUserLimitsErrorList:
    import capo_quicksight.types.batch_describe_user_limits_error

    out: BatchDescribeUserLimitsErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.batch_describe_user_limits_error.deserialize_json(
                item
            )
        )
    return out

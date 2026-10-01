"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSortOrderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iceberg_sort_order

IcebergSortOrderList: TypeAlias = list[
    "capo_glue.types.iceberg_sort_order.IcebergSortOrder"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSortOrderList) -> list:
    import capo_glue.types.iceberg_sort_order

    out: list = []
    for item in value:
        out.append(capo_glue.types.iceberg_sort_order.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IcebergSortOrderList:
    import capo_glue.types.iceberg_sort_order

    out: IcebergSortOrderList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.iceberg_sort_order.deserialize_aws_json_1_1(item))
    return out

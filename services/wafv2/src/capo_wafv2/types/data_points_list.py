"""Generated from Smithy shape ``com.amazonaws.wafv2#DataPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.data_point_entry

DataPointsList: TypeAlias = list["capo_wafv2.types.data_point_entry.DataPointEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataPointsList) -> list:
    import capo_wafv2.types.data_point_entry

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.data_point_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataPointsList:
    import capo_wafv2.types.data_point_entry

    out: DataPointsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wafv2.types.data_point_entry.deserialize_aws_json_1_1(item))
    return out

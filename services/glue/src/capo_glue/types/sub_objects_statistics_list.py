"""Generated from Smithy shape ``com.amazonaws.glue#SubObjectsStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.sub_object_statistics

SubObjectsStatisticsList: TypeAlias = list[
    "capo_glue.types.sub_object_statistics.SubObjectStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubObjectsStatisticsList) -> list:
    import capo_glue.types.sub_object_statistics

    out: list = []
    for item in value:
        out.append(capo_glue.types.sub_object_statistics.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubObjectsStatisticsList:
    import capo_glue.types.sub_object_statistics

    out: SubObjectsStatisticsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.sub_object_statistics.deserialize_aws_json_1_1(item))
    return out

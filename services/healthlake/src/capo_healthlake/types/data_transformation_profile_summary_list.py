"""Generated from Smithy shape ``com.amazonaws.healthlake#DataTransformationProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_profile_summary

DataTransformationProfileSummaryList: TypeAlias = list[
    "capo_healthlake.types.data_transformation_profile_summary.DataTransformationProfileSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataTransformationProfileSummaryList) -> list:
    import capo_healthlake.types.data_transformation_profile_summary

    out: list = []
    for item in value:
        out.append(
            capo_healthlake.types.data_transformation_profile_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DataTransformationProfileSummaryList:
    import capo_healthlake.types.data_transformation_profile_summary

    out: DataTransformationProfileSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_healthlake.types.data_transformation_profile_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out

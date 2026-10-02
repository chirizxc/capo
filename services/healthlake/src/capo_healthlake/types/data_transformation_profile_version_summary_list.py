"""Generated from Smithy shape ``com.amazonaws.healthlake#DataTransformationProfileVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_profile_version_summary

DataTransformationProfileVersionSummaryList: TypeAlias = list[
    "capo_healthlake.types.data_transformation_profile_version_summary.DataTransformationProfileVersionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataTransformationProfileVersionSummaryList) -> list:
    import capo_healthlake.types.data_transformation_profile_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_healthlake.types.data_transformation_profile_version_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DataTransformationProfileVersionSummaryList:
    import capo_healthlake.types.data_transformation_profile_version_summary

    out: DataTransformationProfileVersionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_healthlake.types.data_transformation_profile_version_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out

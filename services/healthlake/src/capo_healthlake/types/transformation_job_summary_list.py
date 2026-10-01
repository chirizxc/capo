"""Generated from Smithy shape ``com.amazonaws.healthlake#TransformationJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_healthlake.types.transformation_job_summary

TransformationJobSummaryList: TypeAlias = list[
    "capo_healthlake.types.transformation_job_summary.TransformationJobSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformationJobSummaryList) -> list:
    import capo_healthlake.types.transformation_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_healthlake.types.transformation_job_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TransformationJobSummaryList:
    import capo_healthlake.types.transformation_job_summary

    out: TransformationJobSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_healthlake.types.transformation_job_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out

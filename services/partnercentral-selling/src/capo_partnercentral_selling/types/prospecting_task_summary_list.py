"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProspectingTaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.prospecting_task_summary

ProspectingTaskSummaryList: TypeAlias = list[
    "capo_partnercentral_selling.types.prospecting_task_summary.ProspectingTaskSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProspectingTaskSummaryList) -> list:
    import capo_partnercentral_selling.types.prospecting_task_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.prospecting_task_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProspectingTaskSummaryList:
    import capo_partnercentral_selling.types.prospecting_task_summary

    out: ProspectingTaskSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.prospecting_task_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out

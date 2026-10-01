"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProspectingFromEngagementTaskSortName``."""

from typing import Literal, TypeAlias, cast

"""<p>The fields available for sorting results from <code>ListProspectingFromEngagementTasks</code>. Valid values are <code>StartTime</code>, <code>TaskName</code>, and <code>FailedEngagementCount</code>.</p>"""
ProspectingFromEngagementTaskSortName: TypeAlias = Literal[
    "StartTime",
    "TaskName",
    "FailedEngagementCount",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProspectingFromEngagementTaskSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProspectingFromEngagementTaskSortName:
    return cast(ProspectingFromEngagementTaskSortName, data)

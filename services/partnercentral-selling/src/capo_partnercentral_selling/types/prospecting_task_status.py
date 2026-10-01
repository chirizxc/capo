"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProspectingTaskStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current execution state of a prospecting task. A task transitions from <code>PENDING</code> to <code>IN_PROGRESS</code> when processing begins, and then to either <code>COMPLETED</code> or <code>FAILED</code> when processing ends.</p>"""
ProspectingTaskStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProspectingTaskStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProspectingTaskStatus:
    return cast(ProspectingTaskStatus, data)

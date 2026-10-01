"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#QualificationsAssociationTaskStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current status of a qualifications association task. Valid values: <code>IN_PROGRESS</code> (task is running), <code>SUCCEEDED</code> (task completed successfully).</p>"""
QualificationsAssociationTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QualificationsAssociationTaskStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QualificationsAssociationTaskStatus:
    return cast(QualificationsAssociationTaskStatus, data)

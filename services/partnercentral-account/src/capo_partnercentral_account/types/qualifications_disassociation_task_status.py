"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#QualificationsDisassociationTaskStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current status of a qualifications disassociation task. Valid values: <code>IN_PROGRESS</code> (task is running), <code>SUCCEEDED</code> (task completed successfully).</p>"""
QualificationsDisassociationTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QualificationsDisassociationTaskStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QualificationsDisassociationTaskStatus:
    return cast(QualificationsDisassociationTaskStatus, data)

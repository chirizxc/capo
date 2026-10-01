"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#QualificationsAssociationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current state of a partner qualifications association. Valid values: <code>ASSOCIATED</code> (the partner is associated with a primary), <code>NOT_ASSOCIATED</code> (the partner has no active association).</p>"""
QualificationsAssociationStatus: TypeAlias = Literal[
    "ASSOCIATED",
    "NOT_ASSOCIATED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QualificationsAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QualificationsAssociationStatus:
    return cast(QualificationsAssociationStatus, data)

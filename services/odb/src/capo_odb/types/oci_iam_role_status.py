"""Generated from Smithy shape ``com.amazonaws.odb#OciIamRoleStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle status of an Amazon Web Services Identity and Access Management (IAM) service role used for Autonomous Database integration with Oracle Cloud Infrastructure (OCI).</p>"""
OciIamRoleStatus: TypeAlias = Literal[
    "PROVISIONING",
    "AVAILABLE",
    "PROVISION_FAILED",
    "TERMINATING",
    "TERMINATE_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciIamRoleStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OciIamRoleStatus:
    return cast(OciIamRoleStatus, data)

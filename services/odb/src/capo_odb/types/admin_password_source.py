"""Generated from Smithy shape ``com.amazonaws.odb#AdminPasswordSource``."""

from typing import Literal, TypeAlias, cast

"""<p>The source of the admin password for an Autonomous Database.</p>"""
AdminPasswordSource: TypeAlias = Literal[
    "CUSTOMER_MANAGED_AWS_SECRET",
    "API_REQUEST_PARAMETER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdminPasswordSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AdminPasswordSource:
    return cast(AdminPasswordSource, data)

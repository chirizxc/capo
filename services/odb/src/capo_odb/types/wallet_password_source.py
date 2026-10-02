"""Generated from Smithy shape ``com.amazonaws.odb#WalletPasswordSource``."""

from typing import Literal, TypeAlias, cast

"""<p>The source of the password for an Autonomous Database wallet.</p>"""
WalletPasswordSource: TypeAlias = Literal[
    "CUSTOMER_MANAGED_AWS_SECRET",
    "API_REQUEST_PARAMETER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WalletPasswordSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WalletPasswordSource:
    return cast(WalletPasswordSource, data)

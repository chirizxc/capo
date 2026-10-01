"""Generated from Smithy shape ``com.amazonaws.billing#BillingDomain``."""

from typing import Literal, TypeAlias, cast

"""<p>The billing domain for a billing view segment. The following values are valid:</p> <ul> <li> <p> <code>PRO_FORMA</code> - Data shaped by Billing Conductor that doesn't reflect the final charges owed to Amazon Web Services.</p> </li> <li> <p> <code>BILLABLE</code> - Data that represents the final charges owed to Amazon Web Services.</p> </li> </ul>"""
BillingDomain: TypeAlias = Literal[
    "BILLABLE",
    "PRO_FORMA",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingDomain) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingDomain:
    return cast(BillingDomain, data)

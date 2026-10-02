"""Generated from Smithy shape ``com.amazonaws.acm#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a certificate update. Possible values:</p> <ul> <li> <p> <code>PENDING_DOMAIN_VALIDATION</code> – The update is waiting for domain validation to complete.</p> </li> <li> <p> <code>SUCCESS</code> – The update completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The update failed.</p> </li> </ul>"""
UpdateStatus: TypeAlias = Literal[
    "PENDING_DOMAIN_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateStatus:
    return cast(UpdateStatus, data)

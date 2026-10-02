"""Generated from Smithy shape ``com.amazonaws.acm#UpdateType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of certificate update. Valid values:</p> <ul> <li> <p> <code>DOMAIN_VALIDATION_METHOD</code> – A change to the domain validation method for the certificate.</p> </li> </ul>"""
UpdateType: TypeAlias = Literal["DOMAIN_VALIDATION_METHOD",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateType:
    return cast(UpdateType, data)

"""Generated from Smithy shape ``com.amazonaws.connect#ContactField``."""

from typing import Literal, TypeAlias, cast

ContactField: TypeAlias = Literal[
    "CUSTOMER_ENDPOINT",
    "ADDITIONAL_EMAIL_RECIPIENTS",
    "EMAIL_SUBJECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactField) -> str:
    return value


def deserialize_json(data: str) -> ContactField:
    return cast(ContactField, data)

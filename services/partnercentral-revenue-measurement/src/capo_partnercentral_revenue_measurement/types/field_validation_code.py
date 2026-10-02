"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#FieldValidationCode``."""

from typing import Literal, TypeAlias, cast

FieldValidationCode: TypeAlias = Literal[
    "REQUIRED_FIELD_MISSING",
    "DUPLICATE_VALUE",
    "INVALID_VALUE",
    "INVALID_STRING_FORMAT",
    "TOO_MANY_VALUES",
    "ACTION_NOT_PERMITTED",
    "INVALID_ENUM_VALUE",
    "INVALID_NUMBER_FORMAT",
    "INVALID_STRING_LENGTH",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FieldValidationCode) -> str:
    return value


def deserialize_cbor(data: str) -> FieldValidationCode:
    return cast(FieldValidationCode, data)

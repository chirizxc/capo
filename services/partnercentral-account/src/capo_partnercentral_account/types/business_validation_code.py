"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#BusinessValidationCode``."""

from typing import Literal, TypeAlias, cast

BusinessValidationCode: TypeAlias = Literal[
    "INCOMPATIBLE_CONNECTION_INVITATION_REQUEST",
    "INCOMPATIBLE_LEGAL_NAME",
    "INCOMPATIBLE_KNOW_YOUR_BUSINESS_STATUS",
    "INCOMPATIBLE_IDENTITY_VERIFICATION_STATUS",
    "INVALID_ACCOUNT_LINKING_STATUS",
    "INVALID_ACCOUNT_STATE",
    "INCOMPATIBLE_DOMAIN",
    "INELIGIBLE_ACCOUNT_TIER",
    "MISSING_ACTIVE_SUBSIDIARY_CONNECTION",
    "INCOMPATIBLE_SUBSIDIARY_CONNECTION",
    "INCOMPATIBLE_PRIMARY_PARTNER",
    "QUALIFICATIONS_ASSOCIATION_LIMIT_EXCEEDED",
    "QUALIFICATIONS_ASSOCIATION_NOT_FOUND",
    "QUALIFICATIONS_ASSOCIATION_EXISTS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessValidationCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BusinessValidationCode:
    return cast(BusinessValidationCode, data)

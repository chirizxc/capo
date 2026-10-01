"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_identifier

EngagementIdentifierList: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> EngagementIdentifierList:
    return [item for item in data if item is not None]

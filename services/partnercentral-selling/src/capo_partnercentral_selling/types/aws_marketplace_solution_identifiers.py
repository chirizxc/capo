"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsMarketplaceSolutionIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_marketplace_solution_identifier

AwsMarketplaceSolutionIdentifiers: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_marketplace_solution_identifier.AwsMarketplaceSolutionIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsMarketplaceSolutionIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AwsMarketplaceSolutionIdentifiers:
    return [item for item in data if item is not None]

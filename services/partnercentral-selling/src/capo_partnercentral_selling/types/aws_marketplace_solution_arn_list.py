"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsMarketplaceSolutionArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_marketplace_solution_arn

AwsMarketplaceSolutionArnList: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_marketplace_solution_arn.AwsMarketplaceSolutionArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsMarketplaceSolutionArnList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AwsMarketplaceSolutionArnList:
    return [item for item in data if item is not None]

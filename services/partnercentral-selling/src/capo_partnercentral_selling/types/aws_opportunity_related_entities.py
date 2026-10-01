"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityRelatedEntities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_marketplace_product_identifiers
    import capo_partnercentral_selling.types.aws_marketplace_solution_identifiers
    import capo_partnercentral_selling.types.aws_product_identifiers
    import capo_partnercentral_selling.types.solution_identifiers


class AwsOpportunityRelatedEntities(TypedDict, closed=True):
    aws_products: NotRequired[
        "capo_partnercentral_selling.types.aws_product_identifiers.AwsProductIdentifiers"
    ]
    """<p>Specifies the AWS products associated with the opportunity. This field helps track the specific products that are part of the proposed solution.</p>"""
    solutions: NotRequired[
        "capo_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
    ]
    """<p>Specifies the partner solutions related to the opportunity. These solutions represent the partner's offerings that are being positioned as part of the overall AWS opportunity.</p>"""
    aws_marketplace_solutions: NotRequired[
        "capo_partnercentral_selling.types.aws_marketplace_solution_identifiers.AwsMarketplaceSolutionIdentifiers"
    ]
    """<p>The AWS Marketplace solution ARNs associated with this opportunity.</p>"""
    aws_marketplace_products: NotRequired[
        "capo_partnercentral_selling.types.aws_marketplace_product_identifiers.AwsMarketplaceProductIdentifiers"
    ]
    """<p>The AWS Marketplace product ARNs associated with this opportunity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityRelatedEntities) -> dict:
    out: dict = {}
    if "aws_products" in value:
        import capo_partnercentral_selling.types.aws_product_identifiers

        out["AwsProducts"] = (
            capo_partnercentral_selling.types.aws_product_identifiers.serialize_aws_json_1_0(
                value["aws_products"]
            )
        )
    if "solutions" in value:
        import capo_partnercentral_selling.types.solution_identifiers

        out["Solutions"] = (
            capo_partnercentral_selling.types.solution_identifiers.serialize_aws_json_1_0(
                value["solutions"]
            )
        )
    if "aws_marketplace_solutions" in value:
        import capo_partnercentral_selling.types.aws_marketplace_solution_identifiers

        out["AwsMarketplaceSolutions"] = (
            capo_partnercentral_selling.types.aws_marketplace_solution_identifiers.serialize_aws_json_1_0(
                value["aws_marketplace_solutions"]
            )
        )
    if "aws_marketplace_products" in value:
        import capo_partnercentral_selling.types.aws_marketplace_product_identifiers

        out["AwsMarketplaceProducts"] = (
            capo_partnercentral_selling.types.aws_marketplace_product_identifiers.serialize_aws_json_1_0(
                value["aws_marketplace_products"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunityRelatedEntities:
    out: AwsOpportunityRelatedEntities = {}  # type: ignore[typeddict-item]
    if data.get("AwsProducts") is not None:
        import capo_partnercentral_selling.types.aws_product_identifiers

        out["aws_products"] = (
            capo_partnercentral_selling.types.aws_product_identifiers.deserialize_aws_json_1_0(
                data["AwsProducts"]
            )
        )
    if data.get("Solutions") is not None:
        import capo_partnercentral_selling.types.solution_identifiers

        out["solutions"] = (
            capo_partnercentral_selling.types.solution_identifiers.deserialize_aws_json_1_0(
                data["Solutions"]
            )
        )
    if data.get("AwsMarketplaceSolutions") is not None:
        import capo_partnercentral_selling.types.aws_marketplace_solution_identifiers

        out["aws_marketplace_solutions"] = (
            capo_partnercentral_selling.types.aws_marketplace_solution_identifiers.deserialize_aws_json_1_0(
                data["AwsMarketplaceSolutions"]
            )
        )
    if data.get("AwsMarketplaceProducts") is not None:
        import capo_partnercentral_selling.types.aws_marketplace_product_identifiers

        out["aws_marketplace_products"] = (
            capo_partnercentral_selling.types.aws_marketplace_product_identifiers.deserialize_aws_json_1_0(
                data["AwsMarketplaceProducts"]
            )
        )
    return out

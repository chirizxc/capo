"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateCommitmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.cost_amount
    import capo_bcm_pricing_calculator.types.purchase_agreement_type
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.uuid


class BillEstimateCommitmentSummary(TypedDict, closed=True):
    id: NotRequired["capo_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier of the commitment. </p>"""
    purchase_agreement_type: NotRequired[
        "capo_bcm_pricing_calculator.types.purchase_agreement_type.PurchaseAgreementType"
    ]
    """<p> The type of purchase agreement (e.g., Reserved Instance, Savings Plan). </p>"""
    offering_id: NotRequired["capo_bcm_pricing_calculator.types.uuid.Uuid"]
    """<p> The identifier of the specific offering associated with this commitment. </p>"""
    usage_account_id: NotRequired[
        "capo_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with this commitment. </p>"""
    region: NotRequired["str"]
    """<p> The Amazon Web Services region associated with this commitment. </p>"""
    term_length: NotRequired["str"]
    """<p> The length of the commitment term. </p>"""
    payment_option: NotRequired["str"]
    """<p> The payment option chosen for this commitment (e.g., All Upfront, Partial Upfront, No Upfront). </p>"""
    upfront_payment: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_amount.CostAmount"
    ]
    """<p> The upfront payment amount for this commitment, if applicable. </p>"""
    monthly_payment: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_amount.CostAmount"
    ]
    """<p> The monthly payment amount for this commitment, if applicable. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateCommitmentSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "purchase_agreement_type" in value:
        import capo_bcm_pricing_calculator.types.purchase_agreement_type

        out["purchaseAgreementType"] = (
            capo_bcm_pricing_calculator.types.purchase_agreement_type.serialize_aws_json_1_0(
                value["purchase_agreement_type"]
            )
        )
    if "offering_id" in value:
        out["offeringId"] = value["offering_id"]
    if "usage_account_id" in value:
        out["usageAccountId"] = value["usage_account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "term_length" in value:
        out["termLength"] = value["term_length"]
    if "payment_option" in value:
        out["paymentOption"] = value["payment_option"]
    if "upfront_payment" in value:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["upfrontPayment"] = (
            capo_bcm_pricing_calculator.types.cost_amount.serialize_aws_json_1_0(
                value["upfront_payment"]
            )
        )
    if "monthly_payment" in value:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["monthlyPayment"] = (
            capo_bcm_pricing_calculator.types.cost_amount.serialize_aws_json_1_0(
                value["monthly_payment"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillEstimateCommitmentSummary:
    out: BillEstimateCommitmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("purchaseAgreementType") is not None:
        import capo_bcm_pricing_calculator.types.purchase_agreement_type

        out["purchase_agreement_type"] = (
            capo_bcm_pricing_calculator.types.purchase_agreement_type.deserialize_aws_json_1_0(
                data["purchaseAgreementType"]
            )
        )
    if data.get("offeringId") is not None:
        out["offering_id"] = data["offeringId"]
    if data.get("usageAccountId") is not None:
        out["usage_account_id"] = data["usageAccountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("termLength") is not None:
        out["term_length"] = data["termLength"]
    if data.get("paymentOption") is not None:
        out["payment_option"] = data["paymentOption"]
    if data.get("upfrontPayment") is not None:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["upfront_payment"] = (
            capo_bcm_pricing_calculator.types.cost_amount.deserialize_aws_json_1_0(
                data["upfrontPayment"]
            )
        )
    if data.get("monthlyPayment") is not None:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["monthly_payment"] = (
            capo_bcm_pricing_calculator.types.cost_amount.deserialize_aws_json_1_0(
                data["monthlyPayment"]
            )
        )
    return out

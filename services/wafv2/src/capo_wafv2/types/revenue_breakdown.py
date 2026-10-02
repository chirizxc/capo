"""Generated from Smithy shape ``com.amazonaws.wafv2#RevenueBreakdown``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.currency
    import capo_wafv2.types.monetization_amount_value
    import capo_wafv2.types.request_count


class RevenueBreakdown(TypedDict, closed=True):
    total_amount: NotRequired[
        "capo_wafv2.types.monetization_amount_value.MonetizationAmountValue"
    ]
    """<p>The total revenue amount in the specified currency.</p>"""
    verified_amount: NotRequired[
        "capo_wafv2.types.monetization_amount_value.MonetizationAmountValue"
    ]
    """<p>The revenue amount from verified AI bots.</p>"""
    unverified_amount: NotRequired[
        "capo_wafv2.types.monetization_amount_value.MonetizationAmountValue"
    ]
    """<p>The revenue amount from unverified AI bots.</p>"""
    currency: NotRequired["capo_wafv2.types.currency.Currency"]
    """<p>The currency of the revenue amounts.</p>"""
    total_settled: "capo_wafv2.types.request_count.RequestCount"
    """<p>The total number of successfully settled payment transactions.</p>"""
    total_monetize_served: "capo_wafv2.types.request_count.RequestCount"
    """<p>The total number of HTTP 402 Payment Required responses served to AI agents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevenueBreakdown) -> dict:
    out: dict = {}
    if "total_amount" in value:
        out["TotalAmount"] = value["total_amount"]
    if "verified_amount" in value:
        out["VerifiedAmount"] = value["verified_amount"]
    if "unverified_amount" in value:
        out["UnverifiedAmount"] = value["unverified_amount"]
    if "currency" in value:
        import capo_wafv2.types.currency

        out["Currency"] = capo_wafv2.types.currency.serialize_aws_json_1_1(
            value["currency"]
        )
    out["TotalSettled"] = value.get("total_settled", 0)
    out["TotalMonetizeServed"] = value.get("total_monetize_served", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> RevenueBreakdown:
    out: RevenueBreakdown = {}  # type: ignore[typeddict-item]
    if data.get("TotalAmount") is not None:
        out["total_amount"] = data["TotalAmount"]
    if data.get("VerifiedAmount") is not None:
        out["verified_amount"] = data["VerifiedAmount"]
    if data.get("UnverifiedAmount") is not None:
        out["unverified_amount"] = data["UnverifiedAmount"]
    if data.get("Currency") is not None:
        import capo_wafv2.types.currency

        out["currency"] = capo_wafv2.types.currency.deserialize_aws_json_1_1(
            data["Currency"]
        )
    if data.get("TotalSettled") is not None:
        out["total_settled"] = data["TotalSettled"]
    else:
        out["total_settled"] = 0
    if data.get("TotalMonetizeServed") is not None:
        out["total_monetize_served"] = data["TotalMonetizeServed"]
    else:
        out["total_monetize_served"] = 0
    return out

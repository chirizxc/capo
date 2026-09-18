"""Generated from Smithy shape ``com.amazonaws.outposts#SubscriptionPricingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.currency_code
    import capo_outposts.types.nullable_float
    import capo_outposts.types.payment_option
    import capo_outposts.types.payment_term


class SubscriptionPricingDetails(TypedDict, closed=True):
    payment_option: NotRequired["capo_outposts.types.payment_option.PaymentOption"]
    """<p>The payment option.</p>"""
    payment_term: NotRequired["capo_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment term.</p>"""
    upfront_price: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The upfront price.</p>"""
    monthly_recurring_price: NotRequired[
        "capo_outposts.types.nullable_float.NullableFloat"
    ]
    """<p>The monthly recurring price.</p>"""
    currency: NotRequired["capo_outposts.types.currency_code.CurrencyCode"]
    """<p>The currency of the price. Currently only <code>USD</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionPricingDetails) -> dict:
    out: dict = {}
    if "payment_option" in value:
        import capo_outposts.types.payment_option

        out["PaymentOption"] = capo_outposts.types.payment_option.serialize_json(
            value["payment_option"]
        )
    if "payment_term" in value:
        import capo_outposts.types.payment_term

        out["PaymentTerm"] = capo_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    if "upfront_price" in value:
        out["UpfrontPrice"] = (
            "NaN"
            if value["upfront_price"] != value["upfront_price"]
            else "Infinity"
            if value["upfront_price"] == float("inf")
            else "-Infinity"
            if value["upfront_price"] == float("-inf")
            else value["upfront_price"]
        )
    if "monthly_recurring_price" in value:
        out["MonthlyRecurringPrice"] = (
            "NaN"
            if value["monthly_recurring_price"] != value["monthly_recurring_price"]
            else "Infinity"
            if value["monthly_recurring_price"] == float("inf")
            else "-Infinity"
            if value["monthly_recurring_price"] == float("-inf")
            else value["monthly_recurring_price"]
        )
    if "currency" in value:
        import capo_outposts.types.currency_code

        out["Currency"] = capo_outposts.types.currency_code.serialize_json(
            value["currency"]
        )
    return out


def deserialize_json(data: dict) -> SubscriptionPricingDetails:
    out: SubscriptionPricingDetails = {}  # type: ignore[typeddict-item]
    if data.get("PaymentOption") is not None:
        import capo_outposts.types.payment_option

        out["payment_option"] = capo_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    if data.get("PaymentTerm") is not None:
        import capo_outposts.types.payment_term

        out["payment_term"] = capo_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    if data.get("UpfrontPrice") is not None:
        out["upfront_price"] = float(data["UpfrontPrice"])
    if data.get("MonthlyRecurringPrice") is not None:
        out["monthly_recurring_price"] = float(data["MonthlyRecurringPrice"])
    if data.get("Currency") is not None:
        import capo_outposts.types.currency_code

        out["currency"] = capo_outposts.types.currency_code.deserialize_json(
            data["Currency"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.invoicing#CurrencyExchangeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string


class CurrencyExchangeDetails(TypedDict, closed=True):
    source_currency_code: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p>The exchange source currency. </p>"""
    target_currency_code: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p>The exchange target currency. </p>"""
    rate: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p>The currency exchange rate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CurrencyExchangeDetails) -> dict:
    out: dict = {}
    if "source_currency_code" in value:
        out["SourceCurrencyCode"] = value["source_currency_code"]
    if "target_currency_code" in value:
        out["TargetCurrencyCode"] = value["target_currency_code"]
    if "rate" in value:
        out["Rate"] = value["rate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CurrencyExchangeDetails:
    out: CurrencyExchangeDetails = {}  # type: ignore[typeddict-item]
    if data.get("SourceCurrencyCode") is not None:
        out["source_currency_code"] = data["SourceCurrencyCode"]
    if data.get("TargetCurrencyCode") is not None:
        out["target_currency_code"] = data["TargetCurrencyCode"]
    if data.get("Rate") is not None:
        out["rate"] = data["Rate"]
    return out

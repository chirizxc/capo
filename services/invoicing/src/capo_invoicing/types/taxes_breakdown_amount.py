"""Generated from Smithy shape ``com.amazonaws.invoicing#TaxesBreakdownAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string


class TaxesBreakdownAmount(TypedDict, closed=True):
    description: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The details of the taxes. </p>"""
    amount: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The tax amount. </p>"""
    rate: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The details of the tax rate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxesBreakdownAmount) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "amount" in value:
        out["Amount"] = value["amount"]
    if "rate" in value:
        out["Rate"] = value["rate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaxesBreakdownAmount:
    out: TaxesBreakdownAmount = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    if data.get("Rate") is not None:
        out["rate"] = data["Rate"]
    return out

"""Generated from Smithy shape ``com.amazonaws.taxsettings#FranceAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.siren_number


class FranceAdditionalInfo(TypedDict, closed=True):
    siren_number: "capo_taxsettings.types.siren_number.SirenNumber"
    """<p>The SIREN number for the company in France. Must be a 9-digit number.</p>"""
    e_invoice_routing_code: NotRequired["str"]
    """<p>The routing code used for electronic invoicing (e-invoicing) for the company in France.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FranceAdditionalInfo) -> dict:
    out: dict = {}
    out["sirenNumber"] = value["siren_number"]
    if "e_invoice_routing_code" in value:
        out["eInvoiceRoutingCode"] = value["e_invoice_routing_code"]
    return out


def deserialize_json(data: dict) -> FranceAdditionalInfo:
    out: FranceAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("sirenNumber") is not None:
        out["siren_number"] = data["sirenNumber"]
    else:
        raise DeserializationError("FranceAdditionalInfo.siren_number required")
    if data.get("eInvoiceRoutingCode") is not None:
        out["e_invoice_routing_code"] = data["eInvoiceRoutingCode"]
    return out

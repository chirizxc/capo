"""Generated from Smithy shape ``com.amazonaws.taxsettings#BelgiumAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.peppol_id


class BelgiumAdditionalInfo(TypedDict, closed=True):
    peppol_id: NotRequired["capo_taxsettings.types.peppol_id.PeppolId"]
    """<p>The Peppol ID for electronic invoicing in Belgium.</p>"""
    is_mercurius_box_enabled: NotRequired["bool"]
    """<p>Indicates whether the Mercurius e-invoicing box is enabled for business-to-government (B2G) invoicing in Belgium.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BelgiumAdditionalInfo) -> dict:
    out: dict = {}
    if "peppol_id" in value:
        out["peppolId"] = value["peppol_id"]
    if "is_mercurius_box_enabled" in value:
        out["isMercuriusBoxEnabled"] = value["is_mercurius_box_enabled"]
    return out


def deserialize_json(data: dict) -> BelgiumAdditionalInfo:
    out: BelgiumAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("peppolId") is not None:
        out["peppol_id"] = data["peppolId"]
    if data.get("isMercuriusBoxEnabled") is not None:
        out["is_mercurius_box_enabled"] = data["isMercuriusBoxEnabled"]
    return out

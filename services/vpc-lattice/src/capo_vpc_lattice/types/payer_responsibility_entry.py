"""Generated from Smithy shape ``com.amazonaws.vpclattice#PayerResponsibilityEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.payer_responsibility_payer
    import capo_vpc_lattice.types.payer_responsibility_scope


class PayerResponsibilityEntry(TypedDict, closed=True):
    scope: NotRequired[
        "capo_vpc_lattice.types.payer_responsibility_scope.PayerResponsibilityScope"
    ]
    """<p>The category of charges that this entry applies to. <code>ResourceGatewayCharges</code> covers the resource gateway's data processing charge.</p>"""
    payer_responsibility_type: NotRequired[
        "capo_vpc_lattice.types.payer_responsibility_payer.PayerResponsibilityPayer"
    ]
    """<p>The account that pays this category of charges. <code>VpcEndpointAccount</code> owns the VPC endpoint. <code>ResourceGatewayAccount</code> owns the resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PayerResponsibilityEntry) -> dict:
    out: dict = {}
    if "scope" in value:
        import capo_vpc_lattice.types.payer_responsibility_scope

        out["scope"] = capo_vpc_lattice.types.payer_responsibility_scope.serialize_json(
            value["scope"]
        )
    if "payer_responsibility_type" in value:
        import capo_vpc_lattice.types.payer_responsibility_payer

        out["payerResponsibilityType"] = (
            capo_vpc_lattice.types.payer_responsibility_payer.serialize_json(
                value["payer_responsibility_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> PayerResponsibilityEntry:
    out: PayerResponsibilityEntry = {}  # type: ignore[typeddict-item]
    if data.get("scope") is not None:
        import capo_vpc_lattice.types.payer_responsibility_scope

        out["scope"] = (
            capo_vpc_lattice.types.payer_responsibility_scope.deserialize_json(
                data["scope"]
            )
        )
    if data.get("payerResponsibilityType") is not None:
        import capo_vpc_lattice.types.payer_responsibility_payer

        out["payer_responsibility_type"] = (
            capo_vpc_lattice.types.payer_responsibility_payer.deserialize_json(
                data["payerResponsibilityType"]
            )
        )
    return out

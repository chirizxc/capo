"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalSuppliers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.procurement_portal_supplier

ProcurementPortalSuppliers: TypeAlias = list[
    "capo_invoicing.types.procurement_portal_supplier.ProcurementPortalSupplier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalSuppliers) -> list:
    import capo_invoicing.types.procurement_portal_supplier

    out: list = []
    for item in value:
        out.append(
            capo_invoicing.types.procurement_portal_supplier.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProcurementPortalSuppliers:
    import capo_invoicing.types.procurement_portal_supplier

    out: ProcurementPortalSuppliers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_invoicing.types.procurement_portal_supplier.deserialize_aws_json_1_0(
                item
            )
        )
    return out

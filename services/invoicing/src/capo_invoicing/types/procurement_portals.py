"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.procurement_portal

ProcurementPortals: TypeAlias = list[
    "capo_invoicing.types.procurement_portal.ProcurementPortal"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortals) -> list:
    import capo_invoicing.types.procurement_portal

    out: list = []
    for item in value:
        out.append(capo_invoicing.types.procurement_portal.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ProcurementPortals:
    import capo_invoicing.types.procurement_portal

    out: ProcurementPortals = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_invoicing.types.procurement_portal.deserialize_aws_json_1_0(item)
        )
    return out

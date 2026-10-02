"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#EntityTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.entity_type

EntityTypeFilterList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.entity_type.EntityType"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityTypeFilterList) -> list:
    import capo_partnercentral_revenue_measurement.types.entity_type

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.entity_type.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> EntityTypeFilterList:
    import capo_partnercentral_revenue_measurement.types.entity_type

    out: EntityTypeFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.entity_type.deserialize_cbor(
                item
            )
        )
    return out

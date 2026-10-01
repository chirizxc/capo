"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#EntityIdentifierFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.entity_identifier

EntityIdentifierFilterList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.entity_identifier.EntityIdentifier"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityIdentifierFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> EntityIdentifierFilterList:
    return [item for item in data if item is not None]

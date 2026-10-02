"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier

RevenueAttributionIdentifierList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionIdentifierList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> RevenueAttributionIdentifierList:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#CreateMarketplaceRevenueShareAllocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.client_token
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id
    import capo_partnercentral_revenue_measurement.types.revenue_share_percent


class CreateMarketplaceRevenueShareAllocationInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog in which to create the allocation.</p>"""
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier for the parent revenue share.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
    ]
    """<p>A unique token to ensure idempotency of the create request.</p>"""
    effective_from: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    """<p>The effective start date for the allocation. Must be the first day of a month.</p>"""
    effective_until: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>The effective end date for the allocation. Must be the last day of a month (YYYY-MM-DD). Omit for open-ended allocations.</p>"""
    revenue_share_percent: "capo_partnercentral_revenue_measurement.types.revenue_share_percent.RevenueSharePercent"
    """<p>The revenue share percentage for this allocation.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateMarketplaceRevenueShareAllocationInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["ProductId"] = value["product_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["EffectiveFrom"] = value["effective_from"]
    if "effective_until" in value:
        out["EffectiveUntil"] = value["effective_until"]
    out["RevenueSharePercent"] = value["revenue_share_percent"]
    return out


def deserialize_cbor(data: dict) -> CreateMarketplaceRevenueShareAllocationInput:
    out: CreateMarketplaceRevenueShareAllocationInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.deserialize_cbor(
                data["Catalog"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMarketplaceRevenueShareAllocationInput.catalog required"
        )
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError(
            "CreateMarketplaceRevenueShareAllocationInput.product_id required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    else:
        raise DeserializationError(
            "CreateMarketplaceRevenueShareAllocationInput.effective_from required"
        )
    if data.get("EffectiveUntil") is not None:
        out["effective_until"] = data["EffectiveUntil"]
    if data.get("RevenueSharePercent") is not None:
        out["revenue_share_percent"] = data["RevenueSharePercent"]
    else:
        raise DeserializationError(
            "CreateMarketplaceRevenueShareAllocationInput.revenue_share_percent required"
        )
    return out

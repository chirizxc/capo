"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#MarketplaceProductSummary``."""

from typing_extensions import NotRequired, TypedDict


class MarketplaceProductSummary(TypedDict, closed=True):
    product_id: NotRequired["str"]
    """<p>The product identifier provided at attribution creation.</p>"""
    product_code: NotRequired["str"]
    """<p>The AWS Marketplace product code resolved using the product identifier.</p>"""
    product_name: NotRequired["str"]
    """<p>The display name of the AWS Marketplace product.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketplaceProductSummary) -> dict:
    out: dict = {}
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "product_code" in value:
        out["ProductCode"] = value["product_code"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    return out


def deserialize_cbor(data: dict) -> MarketplaceProductSummary:
    out: MarketplaceProductSummary = {}  # type: ignore[typeddict-item]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    return out

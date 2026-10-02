"""Generated from Smithy shape ``com.amazonaws.route53resolver#SubscriptionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.product_id
    import capo_route53resolver.types.vendor_name


class SubscriptionInfo(TypedDict, closed=True):
    vendor_name: NotRequired["capo_route53resolver.types.vendor_name.VendorName"]
    """<p>The name of the Amazon Web Services Marketplace seller (vendor) that publishes the partner threat-protection product (for example, <code>Palo Alto Networks</code>).</p>"""
    product_id: NotRequired["capo_route53resolver.types.product_id.ProductId"]
    """<p>The Amazon Web Services Marketplace product identifier of the partner threat-protection product. Use this value to verify or manage the calling account's subscription in Amazon Web Services Marketplace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionInfo) -> dict:
    out: dict = {}
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscriptionInfo:
    out: SubscriptionInfo = {}  # type: ignore[typeddict-item]
    if data.get("VendorName") is not None:
        out["vendor_name"] = data["VendorName"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    return out

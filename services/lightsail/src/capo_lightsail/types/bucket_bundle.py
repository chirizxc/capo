"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.float
    import capo_lightsail.types.integer
    import capo_lightsail.types.non_empty_string


class BucketBundle(TypedDict, closed=True):
    bundle_id: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the bundle.</p>"""
    name: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The name of the bundle.</p>"""
    price: NotRequired["capo_lightsail.types.float.float"]
    """<p>The monthly price of the bundle, in US dollars.</p>"""
    storage_per_month_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The storage size of the bundle, in GB.</p>"""
    transfer_per_month_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The monthly network transfer quota of the bundle.</p>"""
    is_active: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the bundle is active. Use for a new or existing bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketBundle) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "price" in value:
        out["price"] = (
            "NaN"
            if value["price"] != value["price"]
            else "Infinity"
            if value["price"] == float("inf")
            else "-Infinity"
            if value["price"] == float("-inf")
            else value["price"]
        )
    if "storage_per_month_in_gb" in value:
        out["storagePerMonthInGb"] = value["storage_per_month_in_gb"]
    if "transfer_per_month_in_gb" in value:
        out["transferPerMonthInGb"] = value["transfer_per_month_in_gb"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BucketBundle:
    out: BucketBundle = {}  # type: ignore[typeddict-item]
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("price") is not None:
        out["price"] = float(data["price"])
    if data.get("storagePerMonthInGb") is not None:
        out["storage_per_month_in_gb"] = data["storagePerMonthInGb"]
    if data.get("transferPerMonthInGb") is not None:
        out["transfer_per_month_in_gb"] = data["transferPerMonthInGb"]
    if data.get("isActive") is not None:
        out["is_active"] = data["isActive"]
    return out

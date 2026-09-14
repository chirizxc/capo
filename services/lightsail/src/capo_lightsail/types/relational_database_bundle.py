"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.float
    import capo_lightsail.types.integer
    import capo_lightsail.types.string


class RelationalDatabaseBundle(TypedDict, closed=True):
    bundle_id: NotRequired["capo_lightsail.types.string.string"]
    """<p>The ID for the database bundle.</p>"""
    name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name for the database bundle.</p>"""
    price: NotRequired["capo_lightsail.types.float.float"]
    """<p>The cost of the database bundle in US currency.</p>"""
    ram_size_in_gb: NotRequired["capo_lightsail.types.float.float"]
    """<p>The amount of RAM in GB (for example, <code>2.0</code>) for the database bundle.</p>"""
    disk_size_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The size of the disk for the database bundle.</p>"""
    transfer_per_month_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The data transfer rate per month in GB for the database bundle.</p>"""
    cpu_count: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The number of virtual CPUs (vCPUs) for the database bundle.</p>"""
    is_encrypted: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the database bundle is encrypted.</p>"""
    is_active: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the database bundle is active.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseBundle) -> dict:
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
    if "ram_size_in_gb" in value:
        out["ramSizeInGb"] = (
            "NaN"
            if value["ram_size_in_gb"] != value["ram_size_in_gb"]
            else "Infinity"
            if value["ram_size_in_gb"] == float("inf")
            else "-Infinity"
            if value["ram_size_in_gb"] == float("-inf")
            else value["ram_size_in_gb"]
        )
    if "disk_size_in_gb" in value:
        out["diskSizeInGb"] = value["disk_size_in_gb"]
    if "transfer_per_month_in_gb" in value:
        out["transferPerMonthInGb"] = value["transfer_per_month_in_gb"]
    if "cpu_count" in value:
        out["cpuCount"] = value["cpu_count"]
    if "is_encrypted" in value:
        out["isEncrypted"] = value["is_encrypted"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseBundle:
    out: RelationalDatabaseBundle = {}  # type: ignore[typeddict-item]
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("price") is not None:
        out["price"] = float(data["price"])
    if data.get("ramSizeInGb") is not None:
        out["ram_size_in_gb"] = float(data["ramSizeInGb"])
    if data.get("diskSizeInGb") is not None:
        out["disk_size_in_gb"] = data["diskSizeInGb"]
    if data.get("transferPerMonthInGb") is not None:
        out["transfer_per_month_in_gb"] = data["transferPerMonthInGb"]
    if data.get("cpuCount") is not None:
        out["cpu_count"] = data["cpuCount"]
    if data.get("isEncrypted") is not None:
        out["is_encrypted"] = data["isEncrypted"]
    if data.get("isActive") is not None:
        out["is_active"] = data["isActive"]
    return out

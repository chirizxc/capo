"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.boolean
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.vendor_name


class ManagedRuleGroupSummary(TypedDict, closed=True):
    vendor_name: NotRequired["capo_wafv2.types.vendor_name.VendorName"]
    """<p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>"""
    name: NotRequired["capo_wafv2.types.entity_name.EntityName"]
    """<p>The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.</p>"""
    versioning_supported: "capo_wafv2.types.boolean.Boolean"
    """<p>Indicates whether the managed rule group is versioned. If it is, you can retrieve the versions list by calling <a>ListAvailableManagedRuleGroupVersions</a>. </p>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>The description of the managed rule group, provided by Amazon Web Services Managed Rules or the Amazon Web Services Marketplace seller who manages it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleGroupSummary) -> dict:
    out: dict = {}
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    if "name" in value:
        out["Name"] = value["name"]
    out["VersioningSupported"] = value.get("versioning_supported", False)
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleGroupSummary:
    out: ManagedRuleGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("VendorName") is not None:
        out["vendor_name"] = data["VendorName"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VersioningSupported") is not None:
        out["versioning_supported"] = data["VersioningSupported"]
    else:
        out["versioning_supported"] = False
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out

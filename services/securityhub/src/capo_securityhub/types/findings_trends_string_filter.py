"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsTrendsStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.findings_trends_string_field
    import capo_securityhub.types.string_filter


class FindingsTrendsStringFilter(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_securityhub.types.findings_trends_string_field.FindingsTrendsStringField"
    ]
    """<p>The name of the findings field to filter on. You can specify one of the following fields.</p> <ul> <li> <p> <code>account_id</code> – The Amazon Web Services account ID associated with the finding.</p> </li> <li> <p> <code>region</code> – The Amazon Web Services Region associated with the finding.</p> </li> <li> <p> <code>finding_types</code> – The finding types associated with the finding.</p> </li> <li> <p> <code>finding_status</code> – The status of the finding.</p> </li> <li> <p> <code>finding_cve_ids</code> – The Common Vulnerabilities and Exposures (CVE) identifiers associated with the finding.</p> </li> <li> <p> <code>finding_compliance_status</code> – The compliance status of the finding.</p> </li> <li> <p> <code>finding_control_id</code> – The identifier of the security control associated with the finding.</p> </li> <li> <p> <code>finding_class_name</code> – The finding class, such as <code>Compliance Finding</code>.</p> </li> <li> <p> <code>finding_provider</code> – The name of the product that generated the finding.</p> </li> <li> <p> <code>finding_activity_name</code> – The activity name associated with the finding.</p> </li> <li> <p> <code>resource_cloud_providers</code> – The cloud providers of the resources that the finding is associated with. Valid values are <code>AWS</code> and <code>Azure</code>.</p> </li> <li> <p> <code>resource_regions</code> – The Regions of the associated resources. For an Amazon Web Services resource, this is the Amazon Web Services Region. For an Azure resource, this is the Azure Region, such as <code>eastus</code>.</p> </li> <li> <p> <code>resource_owner_ids</code> – The identifiers of the accounts that own the associated resources. For an Amazon Web Services resource, this is the Amazon Web Services account ID. For an Azure resource, this is the Azure subscription ID.</p> </li> <li> <p> <code>resource_owner_organization_ids</code> – The identifiers of the organizations that own the associated resources. For an Amazon Web Services resource, this is the Amazon Web Services organization ID. For an Azure resource, this is the Azure tenant ID.</p> </li> </ul>"""
    filter: NotRequired["capo_securityhub.types.string_filter.StringFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsTrendsStringFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_securityhub.types.findings_trends_string_field

        out["FieldName"] = (
            capo_securityhub.types.findings_trends_string_field.serialize_json(
                value["field_name"]
            )
        )
    if "filter" in value:
        import capo_securityhub.types.string_filter

        out["Filter"] = capo_securityhub.types.string_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> FindingsTrendsStringFilter:
    out: FindingsTrendsStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        import capo_securityhub.types.findings_trends_string_field

        out["field_name"] = (
            capo_securityhub.types.findings_trends_string_field.deserialize_json(
                data["FieldName"]
            )
        )
    if data.get("Filter") is not None:
        import capo_securityhub.types.string_filter

        out["filter"] = capo_securityhub.types.string_filter.deserialize_json(
            data["Filter"]
        )
    return out

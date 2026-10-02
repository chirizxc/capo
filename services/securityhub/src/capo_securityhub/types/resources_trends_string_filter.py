"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.resources_trends_string_field
    import capo_securityhub.types.string_filter


class ResourcesTrendsStringFilter(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_securityhub.types.resources_trends_string_field.ResourcesTrendsStringField"
    ]
    """<p>The name of the resources field to filter on. You can specify one of the following fields.</p> <ul> <li> <p> <code>account_id</code> – The Amazon Web Services account ID that owns the resource.</p> </li> <li> <p> <code>region</code> – The Amazon Web Services Region of the resource.</p> </li> <li> <p> <code>resource_type</code> – The type of the resource.</p> </li> <li> <p> <code>resource_category</code> – The category of the resource.</p> </li> <li> <p> <code>resource_cloud_provider</code> – The cloud provider of the resource. Valid values are <code>AWS</code> and <code>Azure</code>.</p> </li> <li> <p> <code>resource_region</code> – The Region of the resource. For an Amazon Web Services resource, this is the Amazon Web Services Region. For an Azure resource, this is the Azure Region, such as <code>eastus</code>.</p> </li> <li> <p> <code>resource_owner_id</code> – The identifier of the account that owns the resource. For an Amazon Web Services resource, this is the Amazon Web Services account ID. For an Azure resource, this is the Azure subscription ID.</p> </li> <li> <p> <code>resource_owner_organization_id</code> – The identifier of the organization that owns the resource. For an Amazon Web Services resource, this is the Amazon Web Services organization ID. For an Azure resource, this is the Azure tenant ID.</p> </li> </ul>"""
    filter: NotRequired["capo_securityhub.types.string_filter.StringFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsStringFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_securityhub.types.resources_trends_string_field

        out["FieldName"] = (
            capo_securityhub.types.resources_trends_string_field.serialize_json(
                value["field_name"]
            )
        )
    if "filter" in value:
        import capo_securityhub.types.string_filter

        out["Filter"] = capo_securityhub.types.string_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesTrendsStringFilter:
    out: ResourcesTrendsStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        import capo_securityhub.types.resources_trends_string_field

        out["field_name"] = (
            capo_securityhub.types.resources_trends_string_field.deserialize_json(
                data["FieldName"]
            )
        )
    if data.get("Filter") is not None:
        import capo_securityhub.types.string_filter

        out["filter"] = capo_securityhub.types.string_filter.deserialize_json(
            data["Filter"]
        )
    return out

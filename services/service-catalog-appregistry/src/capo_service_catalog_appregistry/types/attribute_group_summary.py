"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AttributeGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.attribute_group_arn
    import capo_service_catalog_appregistry.types.attribute_group_id
    import capo_service_catalog_appregistry.types.created_by
    import capo_service_catalog_appregistry.types.description
    import capo_service_catalog_appregistry.types.name
    import capo_service_catalog_appregistry.types.timestamp


class AttributeGroupSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_service_catalog_appregistry.types.attribute_group_id.AttributeGroupId"
    ]
    """<p>The globally unique attribute group identifier of the attribute group.</p>"""
    arn: NotRequired[
        "capo_service_catalog_appregistry.types.attribute_group_arn.AttributeGroupArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the attribute group across services.</p>"""
    name: NotRequired["capo_service_catalog_appregistry.types.name.Name"]
    """<p>The name of the attribute group.</p>"""
    description: NotRequired[
        "capo_service_catalog_appregistry.types.description.Description"
    ]
    """<p>The description of the attribute group that the user provides.</p>"""
    creation_time: NotRequired[
        "capo_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p>The ISO-8601 formatted timestamp of the moment the attribute group was created.</p>"""
    last_update_time: NotRequired[
        "capo_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p>The ISO-8601 formatted timestamp of the moment the attribute group was last updated. This time is the same as the creationTime for a newly created attribute group.</p>"""
    created_by: NotRequired[
        "capo_service_catalog_appregistry.types.created_by.CreatedBy"
    ]
    """<p>The service principal that created the attribute group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeGroupSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_time" in value:
        import capo_service_catalog_appregistry.types.timestamp

        out["creationTime"] = (
            capo_service_catalog_appregistry.types.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_update_time" in value:
        import capo_service_catalog_appregistry.types.timestamp

        out["lastUpdateTime"] = (
            capo_service_catalog_appregistry.types.timestamp.serialize_json(
                value["last_update_time"]
            )
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> AttributeGroupSummary:
    out: AttributeGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creationTime") is not None:
        import capo_service_catalog_appregistry.types.timestamp

        out["creation_time"] = (
            capo_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("lastUpdateTime") is not None:
        import capo_service_catalog_appregistry.types.timestamp

        out["last_update_time"] = (
            capo_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["lastUpdateTime"]
            )
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    return out

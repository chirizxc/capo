"""Generated from Smithy shape ``com.amazonaws.glue#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.category
    import capo_glue.types.custom_properties
    import capo_glue.types.entity_description
    import capo_glue.types.entity_label
    import capo_glue.types.entity_name
    import capo_glue.types.is_parent_entity


class Entity(TypedDict, closed=True):
    entity_name: NotRequired["capo_glue.types.entity_name.EntityName"]
    """<p>The name of the entity.</p>"""
    label: NotRequired["capo_glue.types.entity_label.EntityLabel"]
    """<p>Label used for the entity.</p>"""
    is_parent_entity: NotRequired["capo_glue.types.is_parent_entity.IsParentEntity"]
    """<p>A Boolean value which helps to determine whether there are sub objects that can be listed.</p>"""
    description: NotRequired["capo_glue.types.entity_description.EntityDescription"]
    """<p>A description of the entity.</p>"""
    category: NotRequired["capo_glue.types.category.Category"]
    """<p>The type of entities that are present in the response. This value depends on the source connection. For example this is <code>SObjects</code> for Salesforce and <code>databases</code> or <code>schemas</code> or <code>tables</code> for sources like Amazon Redshift.</p>"""
    custom_properties: NotRequired["capo_glue.types.custom_properties.CustomProperties"]
    """<p>An optional map of keys which may be returned for an entity by a connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entity) -> dict:
    out: dict = {}
    if "entity_name" in value:
        out["EntityName"] = value["entity_name"]
    if "label" in value:
        out["Label"] = value["label"]
    if "is_parent_entity" in value:
        out["IsParentEntity"] = value["is_parent_entity"]
    if "description" in value:
        out["Description"] = value["description"]
    if "category" in value:
        out["Category"] = value["category"]
    if "custom_properties" in value:
        import capo_glue.types.custom_properties

        out["CustomProperties"] = (
            capo_glue.types.custom_properties.serialize_aws_json_1_1(
                value["custom_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if data.get("EntityName") is not None:
        out["entity_name"] = data["EntityName"]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("IsParentEntity") is not None:
        out["is_parent_entity"] = data["IsParentEntity"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("CustomProperties") is not None:
        import capo_glue.types.custom_properties

        out["custom_properties"] = (
            capo_glue.types.custom_properties.deserialize_aws_json_1_1(
                data["CustomProperties"]
            )
        )
    return out

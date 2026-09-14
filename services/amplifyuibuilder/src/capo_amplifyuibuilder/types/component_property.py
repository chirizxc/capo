"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_condition_property
    import capo_amplifyuibuilder.types.component_property_binding_properties
    import capo_amplifyuibuilder.types.component_property_list
    import capo_amplifyuibuilder.types.form_bindings


class ComponentProperty(TypedDict, closed=True):
    value: NotRequired["str"]
    """<p>The value to assign to the component property.</p>"""
    binding_properties: NotRequired[
        "capo_amplifyuibuilder.types.component_property_binding_properties.ComponentPropertyBindingProperties"
    ]
    """<p>The information to bind the component property to data at runtime.</p>"""
    collection_binding_properties: NotRequired[
        "capo_amplifyuibuilder.types.component_property_binding_properties.ComponentPropertyBindingProperties"
    ]
    """<p>The information to bind the component property to data at runtime. Use this for collection components.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value to assign to the component property.</p>"""
    model: NotRequired["str"]
    """<p>The data model to use to assign a value to the component property.</p>"""
    bindings: NotRequired["capo_amplifyuibuilder.types.form_bindings.FormBindings"]
    """<p>The information to bind the component property to form data.</p>"""
    event: NotRequired["str"]
    """<p>An event that occurs in your app. Use this for workflow data binding.</p>"""
    user_attribute: NotRequired["str"]
    """<p>An authenticated user attribute to use to assign a value to the component property.</p>"""
    concat: NotRequired[
        "capo_amplifyuibuilder.types.component_property_list.ComponentPropertyList"
    ]
    """<p>A list of component properties to concatenate to create the value to assign to this component property.</p>"""
    condition: NotRequired[
        "capo_amplifyuibuilder.types.component_condition_property.ComponentConditionProperty"
    ]
    """<p>The conditional expression to use to assign a value to the component property.</p>"""
    configured: NotRequired["bool"]
    """<p>Specifies whether the user configured the property in Amplify Studio after importing it.</p>"""
    type: NotRequired["str"]
    """<p>The component type.</p>"""
    imported_value: NotRequired["str"]
    """<p>The default value assigned to the property when the component is imported into an app.</p>"""
    component_name: NotRequired["str"]
    """<p>The name of the component that is affected by an event.</p>"""
    property: NotRequired["str"]
    """<p>The name of the component's property that is affected by an event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentProperty) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "binding_properties" in value:
        import capo_amplifyuibuilder.types.component_property_binding_properties

        out["bindingProperties"] = (
            capo_amplifyuibuilder.types.component_property_binding_properties.serialize_json(
                value["binding_properties"]
            )
        )
    if "collection_binding_properties" in value:
        import capo_amplifyuibuilder.types.component_property_binding_properties

        out["collectionBindingProperties"] = (
            capo_amplifyuibuilder.types.component_property_binding_properties.serialize_json(
                value["collection_binding_properties"]
            )
        )
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "model" in value:
        out["model"] = value["model"]
    if "bindings" in value:
        import capo_amplifyuibuilder.types.form_bindings

        out["bindings"] = capo_amplifyuibuilder.types.form_bindings.serialize_json(
            value["bindings"]
        )
    if "event" in value:
        out["event"] = value["event"]
    if "user_attribute" in value:
        out["userAttribute"] = value["user_attribute"]
    if "concat" in value:
        import capo_amplifyuibuilder.types.component_property_list

        out["concat"] = (
            capo_amplifyuibuilder.types.component_property_list.serialize_json(
                value["concat"]
            )
        )
    if "condition" in value:
        import capo_amplifyuibuilder.types.component_condition_property

        out["condition"] = (
            capo_amplifyuibuilder.types.component_condition_property.serialize_json(
                value["condition"]
            )
        )
    if "configured" in value:
        out["configured"] = value["configured"]
    if "type" in value:
        out["type"] = value["type"]
    if "imported_value" in value:
        out["importedValue"] = value["imported_value"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "property" in value:
        out["property"] = value["property"]
    return out


def deserialize_json(data: dict) -> ComponentProperty:
    out: ComponentProperty = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("bindingProperties") is not None:
        import capo_amplifyuibuilder.types.component_property_binding_properties

        out["binding_properties"] = (
            capo_amplifyuibuilder.types.component_property_binding_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    if data.get("collectionBindingProperties") is not None:
        import capo_amplifyuibuilder.types.component_property_binding_properties

        out["collection_binding_properties"] = (
            capo_amplifyuibuilder.types.component_property_binding_properties.deserialize_json(
                data["collectionBindingProperties"]
            )
        )
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("model") is not None:
        out["model"] = data["model"]
    if data.get("bindings") is not None:
        import capo_amplifyuibuilder.types.form_bindings

        out["bindings"] = capo_amplifyuibuilder.types.form_bindings.deserialize_json(
            data["bindings"]
        )
    if data.get("event") is not None:
        out["event"] = data["event"]
    if data.get("userAttribute") is not None:
        out["user_attribute"] = data["userAttribute"]
    if data.get("concat") is not None:
        import capo_amplifyuibuilder.types.component_property_list

        out["concat"] = (
            capo_amplifyuibuilder.types.component_property_list.deserialize_json(
                data["concat"]
            )
        )
    if data.get("condition") is not None:
        import capo_amplifyuibuilder.types.component_condition_property

        out["condition"] = (
            capo_amplifyuibuilder.types.component_condition_property.deserialize_json(
                data["condition"]
            )
        )
    if data.get("configured") is not None:
        out["configured"] = data["configured"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("importedValue") is not None:
        out["imported_value"] = data["importedValue"]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("property") is not None:
        out["property"] = data["property"]
    return out

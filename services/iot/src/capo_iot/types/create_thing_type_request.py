"""Generated from Smithy shape ``com.amazonaws.iot#CreateThingTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.tag_list
    import capo_iot.types.thing_type_name
    import capo_iot.types.thing_type_properties


class CreateThingTypeRequest(TypedDict, closed=True):
    thing_type_name: "capo_iot.types.thing_type_name.ThingTypeName"
    """<p>The name of the thing type.</p>"""
    thing_type_properties: NotRequired[
        "capo_iot.types.thing_type_properties.ThingTypeProperties"
    ]
    """<p>The ThingTypeProperties for the thing type to create. It contains information about the new thing type including a description, and a list of searchable thing attribute names.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the thing type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThingTypeRequest) -> dict:
    out: dict = {}
    if "thing_type_properties" in value:
        import capo_iot.types.thing_type_properties

        out["thingTypeProperties"] = (
            capo_iot.types.thing_type_properties.serialize_json(
                value["thing_type_properties"]
            )
        )
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateThingTypeRequest:
    out: CreateThingTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("thingTypeProperties") is not None:
        import capo_iot.types.thing_type_properties

        out["thing_type_properties"] = (
            capo_iot.types.thing_type_properties.deserialize_json(
                data["thingTypeProperties"]
            )
        )
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out

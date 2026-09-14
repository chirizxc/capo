"""Generated from Smithy shape ``com.amazonaws.appsync#Type``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_name
    import capo_appsync.types.string
    import capo_appsync.types.type_definition_format


class Type(TypedDict, closed=True):
    name: NotRequired["capo_appsync.types.resource_name.ResourceName"]
    """<p>The type name.</p>"""
    description: NotRequired["capo_appsync.types.string.String"]
    """<p>The type description.</p>"""
    arn: NotRequired["capo_appsync.types.string.String"]
    """<p>The type Amazon Resource Name (ARN).</p>"""
    definition: NotRequired["capo_appsync.types.string.String"]
    """<p>The type definition.</p>"""
    format: NotRequired[
        "capo_appsync.types.type_definition_format.TypeDefinitionFormat"
    ]
    """<p>The type format: SDL or JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Type) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "definition" in value:
        out["definition"] = value["definition"]
    if "format" in value:
        import capo_appsync.types.type_definition_format

        out["format"] = capo_appsync.types.type_definition_format.serialize_json(
            value["format"]
        )
    return out


def deserialize_json(data: dict) -> Type:
    out: Type = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    if data.get("format") is not None:
        import capo_appsync.types.type_definition_format

        out["format"] = capo_appsync.types.type_definition_format.deserialize_json(
            data["format"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.opensearch#ExportOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.saved_object_identifier_list
    import capo_opensearch.types.string_list


class ExportOptions(TypedDict, closed=True):
    types: NotRequired["capo_opensearch.types.string_list.StringList"]
    """<p>A list of saved object types to include in the migration. Valid values include <code>dashboard</code>, <code>visualization</code>, <code>index-pattern</code>, <code>search</code>, and <code>query</code>.</p>"""
    objects: NotRequired[
        "capo_opensearch.types.saved_object_identifier_list.SavedObjectIdentifierList"
    ]
    """<p>A list of specific saved objects to include in the migration, identified by type and ID.</p>"""
    include_references_deep: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Specifies whether to include all objects referenced by the exported objects, recursively.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportOptions) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_opensearch.types.string_list

        out["types"] = capo_opensearch.types.string_list.serialize_json(value["types"])
    if "objects" in value:
        import capo_opensearch.types.saved_object_identifier_list

        out["objects"] = (
            capo_opensearch.types.saved_object_identifier_list.serialize_json(
                value["objects"]
            )
        )
    if "include_references_deep" in value:
        out["includeReferencesDeep"] = value["include_references_deep"]
    return out


def deserialize_json(data: dict) -> ExportOptions:
    out: ExportOptions = {}  # type: ignore[typeddict-item]
    if data.get("types") is not None:
        import capo_opensearch.types.string_list

        out["types"] = capo_opensearch.types.string_list.deserialize_json(data["types"])
    if data.get("objects") is not None:
        import capo_opensearch.types.saved_object_identifier_list

        out["objects"] = (
            capo_opensearch.types.saved_object_identifier_list.deserialize_json(
                data["objects"]
            )
        )
    if data.get("includeReferencesDeep") is not None:
        out["include_references_deep"] = data["includeReferencesDeep"]
    return out

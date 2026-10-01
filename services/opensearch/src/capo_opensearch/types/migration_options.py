"""Generated from Smithy shape ``com.amazonaws.opensearch#MigrationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.export_options
    import capo_opensearch.types.migration_source
    import capo_opensearch.types.migration_workspace
    import capo_opensearch.types.string


class MigrationOptions(TypedDict, closed=True):
    source: "capo_opensearch.types.migration_source.MigrationSource"
    """<p>The data source from which to export saved objects.</p>"""
    workspace: "capo_opensearch.types.migration_workspace.MigrationWorkspace"
    """<p>The target workspace configuration for importing saved objects. You can specify an existing workspace or request creation of a new workspace.</p>"""
    export_options: NotRequired["capo_opensearch.types.export_options.ExportOptions"]
    """<p>Options to filter the scope of saved objects to export from the source.</p>"""
    conflict_resolution: NotRequired["capo_opensearch.types.string.String"]
    """<p>The strategy for resolving conflicts when saved objects already exist in the target workspace. Valid values are <code>CREATE_NEW_COPIES</code>, which creates new objects with unique IDs, and <code>overwrite</code>, which replaces existing objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationOptions) -> dict:
    out: dict = {}
    import capo_opensearch.types.migration_source

    out["source"] = capo_opensearch.types.migration_source.serialize_json(
        value["source"]
    )
    import capo_opensearch.types.migration_workspace

    out["workspace"] = capo_opensearch.types.migration_workspace.serialize_json(
        value["workspace"]
    )
    if "export_options" in value:
        import capo_opensearch.types.export_options

        out["exportOptions"] = capo_opensearch.types.export_options.serialize_json(
            value["export_options"]
        )
    if "conflict_resolution" in value:
        out["conflictResolution"] = value["conflict_resolution"]
    return out


def deserialize_json(data: dict) -> MigrationOptions:
    out: MigrationOptions = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_opensearch.types.migration_source

        out["source"] = capo_opensearch.types.migration_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("MigrationOptions.source required")
    if data.get("workspace") is not None:
        import capo_opensearch.types.migration_workspace

        out["workspace"] = capo_opensearch.types.migration_workspace.deserialize_json(
            data["workspace"]
        )
    else:
        raise DeserializationError("MigrationOptions.workspace required")
    if data.get("exportOptions") is not None:
        import capo_opensearch.types.export_options

        out["export_options"] = capo_opensearch.types.export_options.deserialize_json(
            data["exportOptions"]
        )
    if data.get("conflictResolution") is not None:
        out["conflict_resolution"] = data["conflictResolution"]
    return out

"""Generated from Smithy shape ``com.amazonaws.amp#ExporterConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_amp.types.open_search_exporter_configuration


class _ExporterConfiguration_openSearchConfiguration(TypedDict, closed=True):
    openSearchConfiguration: "capo_amp.types.open_search_exporter_configuration.OpenSearchExporterConfiguration"


ExporterConfiguration: TypeAlias = _ExporterConfiguration_openSearchConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: ExporterConfiguration) -> dict:
    if "openSearchConfiguration" in value:
        import capo_amp.types.open_search_exporter_configuration

        return {
            "openSearchConfiguration": capo_amp.types.open_search_exporter_configuration.serialize_json(
                value["openSearchConfiguration"]
            )
        }
    else:
        raise SerializationError("ExporterConfiguration: no variant present")


def deserialize_json(data: dict) -> ExporterConfiguration:
    if data.get("openSearchConfiguration") is not None:
        import capo_amp.types.open_search_exporter_configuration

        return {
            "openSearchConfiguration": capo_amp.types.open_search_exporter_configuration.deserialize_json(
                data["openSearchConfiguration"]
            )
        }
    else:
        raise DeserializationError("ExporterConfiguration: no recognized variant key")

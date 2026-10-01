"""Generated from Smithy shape ``com.amazonaws.amp#ExporterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amp.types.exporter_configuration

ExporterList: TypeAlias = list[
    "capo_amp.types.exporter_configuration.ExporterConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExporterList) -> list:
    import capo_amp.types.exporter_configuration

    out: list = []
    for item in value:
        out.append(capo_amp.types.exporter_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExporterList:
    import capo_amp.types.exporter_configuration

    out: ExporterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_amp.types.exporter_configuration.deserialize_json(item))
    return out

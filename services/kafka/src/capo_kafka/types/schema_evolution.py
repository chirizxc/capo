"""Generated from Smithy shape ``com.amazonaws.kafka#SchemaEvolution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean


class SchemaEvolution(TypedDict, closed=True):
    enable_schema_evolution: NotRequired["capo_kafka.types.__boolean.__boolean"]
    """<p>Whether to allow MSK to evolve the destination table's schema. Must be false for the current release.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaEvolution) -> dict:
    out: dict = {}
    if "enable_schema_evolution" in value:
        out["enableSchemaEvolution"] = value["enable_schema_evolution"]
    return out


def deserialize_json(data: dict) -> SchemaEvolution:
    out: SchemaEvolution = {}  # type: ignore[typeddict-item]
    if data.get("enableSchemaEvolution") is not None:
        out["enable_schema_evolution"] = data["enableSchemaEvolution"]
    return out

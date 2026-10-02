"""Generated from Smithy shape ``com.amazonaws.kafka#TableCreation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean


class TableCreation(TypedDict, closed=True):
    enable_table_creation: NotRequired["capo_kafka.types.__boolean.__boolean"]
    """<p>Whether MSK creates the destination table on the customer's behalf. Must be true for the current release.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableCreation) -> dict:
    out: dict = {}
    if "enable_table_creation" in value:
        out["enableTableCreation"] = value["enable_table_creation"]
    return out


def deserialize_json(data: dict) -> TableCreation:
    out: TableCreation = {}  # type: ignore[typeddict-item]
    if data.get("enableTableCreation") is not None:
        out["enable_table_creation"] = data["enableTableCreation"]
    return out

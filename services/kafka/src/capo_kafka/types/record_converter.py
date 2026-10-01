"""Generated from Smithy shape ``com.amazonaws.kafka#RecordConverter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.value_converter


class RecordConverter(TypedDict, closed=True):
    value_converter: NotRequired["capo_kafka.types.value_converter.ValueConverter"]
    """<p>The deserialization format applied to Apache Kafka record values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordConverter) -> dict:
    out: dict = {}
    if "value_converter" in value:
        import capo_kafka.types.value_converter

        out["valueConverter"] = capo_kafka.types.value_converter.serialize_json(
            value["value_converter"]
        )
    return out


def deserialize_json(data: dict) -> RecordConverter:
    out: RecordConverter = {}  # type: ignore[typeddict-item]
    if data.get("valueConverter") is not None:
        import capo_kafka.types.value_converter

        out["value_converter"] = capo_kafka.types.value_converter.deserialize_json(
            data["valueConverter"]
        )
    return out

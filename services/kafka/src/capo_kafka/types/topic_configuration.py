"""Generated from Smithy shape ``com.amazonaws.kafka#TopicConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.record_converter
    import capo_kafka.types.record_schema


class TopicConfiguration(TypedDict, closed=True):
    record_converter: NotRequired["capo_kafka.types.record_converter.RecordConverter"]
    """<p>Configuration that controls how Apache Kafka record values are deserialized for the destination.</p>"""
    record_schema: NotRequired["capo_kafka.types.record_schema.RecordSchema"]
    """<p>The schema used to validate records when the value converter requires one (for example, JSON_SCHEMA_GSR).</p>"""
    topic_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicConfiguration) -> dict:
    out: dict = {}
    if "record_converter" in value:
        import capo_kafka.types.record_converter

        out["recordConverter"] = capo_kafka.types.record_converter.serialize_json(
            value["record_converter"]
        )
    if "record_schema" in value:
        import capo_kafka.types.record_schema

        out["recordSchema"] = capo_kafka.types.record_schema.serialize_json(
            value["record_schema"]
        )
    if "topic_arn" in value:
        out["topicArn"] = value["topic_arn"]
    return out


def deserialize_json(data: dict) -> TopicConfiguration:
    out: TopicConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("recordConverter") is not None:
        import capo_kafka.types.record_converter

        out["record_converter"] = capo_kafka.types.record_converter.deserialize_json(
            data["recordConverter"]
        )
    if data.get("recordSchema") is not None:
        import capo_kafka.types.record_schema

        out["record_schema"] = capo_kafka.types.record_schema.deserialize_json(
            data["recordSchema"]
        )
    if data.get("topicArn") is not None:
        out["topic_arn"] = data["topicArn"]
    return out

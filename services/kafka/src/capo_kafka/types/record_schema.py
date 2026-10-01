"""Generated from Smithy shape ``com.amazonaws.kafka#RecordSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class RecordSchema(TypedDict, closed=True):
    gsr_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the AWS Glue Schema Registry schema (not registry) used to validate records for the destination Apache Iceberg table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordSchema) -> dict:
    out: dict = {}
    if "gsr_arn" in value:
        out["gsrArn"] = value["gsr_arn"]
    return out


def deserialize_json(data: dict) -> RecordSchema:
    out: RecordSchema = {}  # type: ignore[typeddict-item]
    if data.get("gsrArn") is not None:
        out["gsr_arn"] = data["gsrArn"]
    return out

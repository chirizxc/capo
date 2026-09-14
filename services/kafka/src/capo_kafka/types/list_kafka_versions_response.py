"""Generated from Smithy shape ``com.amazonaws.kafka#ListKafkaVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_kafka_version
    import capo_kafka.types.__string


class ListKafkaVersionsResponse(TypedDict, closed=True):
    kafka_versions: NotRequired[
        "capo_kafka.types.__list_of_kafka_version.__listOfKafkaVersion"
    ]
    next_token: NotRequired["capo_kafka.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListKafkaVersionsResponse) -> dict:
    out: dict = {}
    if "kafka_versions" in value:
        import capo_kafka.types.__list_of_kafka_version

        out["kafkaVersions"] = capo_kafka.types.__list_of_kafka_version.serialize_json(
            value["kafka_versions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKafkaVersionsResponse:
    out: ListKafkaVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("kafkaVersions") is not None:
        import capo_kafka.types.__list_of_kafka_version

        out["kafka_versions"] = (
            capo_kafka.types.__list_of_kafka_version.deserialize_json(
                data["kafkaVersions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

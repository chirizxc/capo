"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EnrichmentJobConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.event_detection


class _EnrichmentJobConfiguration_eventDetection(TypedDict, closed=True):
    eventDetection: "capo_iotsitewise.types.event_detection.EventDetection"


EnrichmentJobConfiguration: TypeAlias = _EnrichmentJobConfiguration_eventDetection


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentJobConfiguration) -> dict:
    if "eventDetection" in value:
        import capo_iotsitewise.types.event_detection

        return {
            "eventDetection": capo_iotsitewise.types.event_detection.serialize_json(
                value["eventDetection"]
            )
        }
    else:
        raise SerializationError("EnrichmentJobConfiguration: no variant present")


def deserialize_json(data: dict) -> EnrichmentJobConfiguration:
    if data.get("eventDetection") is not None:
        import capo_iotsitewise.types.event_detection

        return {
            "eventDetection": capo_iotsitewise.types.event_detection.deserialize_json(
                data["eventDetection"]
            )
        }
    else:
        raise DeserializationError(
            "EnrichmentJobConfiguration: no recognized variant key"
        )

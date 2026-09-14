"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorMissingDataAction``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError


class _AnomalyDetectorMissingDataAction_markAsAnomaly(TypedDict, closed=True):
    markAsAnomaly: "bool"


class _AnomalyDetectorMissingDataAction_skip(TypedDict, closed=True):
    skip: "bool"


AnomalyDetectorMissingDataAction: TypeAlias = (
    _AnomalyDetectorMissingDataAction_markAsAnomaly
    | _AnomalyDetectorMissingDataAction_skip
)


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorMissingDataAction) -> dict:
    if "markAsAnomaly" in value:
        return {"markAsAnomaly": value["markAsAnomaly"]}
    elif "skip" in value:
        return {"skip": value["skip"]}
    else:
        raise SerializationError("AnomalyDetectorMissingDataAction: no variant present")


def deserialize_json(data: dict) -> AnomalyDetectorMissingDataAction:
    if data.get("markAsAnomaly") is not None:
        return {"markAsAnomaly": data["markAsAnomaly"]}
    elif data.get("skip") is not None:
        return {"skip": data["skip"]}
    else:
        raise DeserializationError(
            "AnomalyDetectorMissingDataAction: no recognized variant key"
        )

"""Generated from Smithy shape ``com.amazonaws.securityagent#DiffSource``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError


class _DiffSource_s3Uri(TypedDict, closed=True):
    s3Uri: "str"


DiffSource: TypeAlias = _DiffSource_s3Uri


# --- restJson1 ser/de ---
def serialize_json(value: DiffSource) -> dict:
    if "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("DiffSource: no variant present")


def deserialize_json(data: dict) -> DiffSource:
    if data.get("s3Uri") is not None:
        return {"s3Uri": data["s3Uri"]}
    else:
        raise DeserializationError("DiffSource: no recognized variant key")

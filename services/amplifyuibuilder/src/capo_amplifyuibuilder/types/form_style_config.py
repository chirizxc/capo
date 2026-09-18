"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormStyleConfig``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError, SerializationError


class _FormStyleConfig_tokenReference(TypedDict, closed=True):
    tokenReference: "str"


class _FormStyleConfig_value(TypedDict, closed=True):
    value: "str"


FormStyleConfig: TypeAlias = _FormStyleConfig_tokenReference | _FormStyleConfig_value


# --- restJson1 ser/de ---
def serialize_json(value: FormStyleConfig) -> dict:
    if "tokenReference" in value:
        return {"tokenReference": value["tokenReference"]}
    elif "value" in value:
        return {"value": value["value"]}
    else:
        raise SerializationError("FormStyleConfig: no variant present")


def deserialize_json(data: dict) -> FormStyleConfig:
    if data.get("tokenReference") is not None:
        return {"tokenReference": data["tokenReference"]}
    elif data.get("value") is not None:
        return {"value": data["value"]}
    else:
        raise DeserializationError("FormStyleConfig: no recognized variant key")

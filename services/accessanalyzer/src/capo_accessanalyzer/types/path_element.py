"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PathElement``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.substring


class _PathElement_index(TypedDict, closed=True):
    index: "int"


class _PathElement_key(TypedDict, closed=True):
    key: "str"


class _PathElement_substring(TypedDict, closed=True):
    substring: "capo_accessanalyzer.types.substring.Substring"


class _PathElement_value(TypedDict, closed=True):
    value: "str"


PathElement: TypeAlias = (
    _PathElement_index | _PathElement_key | _PathElement_substring | _PathElement_value
)


# --- restJson1 ser/de ---
def serialize_json(value: PathElement) -> dict:
    if "index" in value:
        return {"index": value["index"]}
    elif "key" in value:
        return {"key": value["key"]}
    elif "substring" in value:
        import capo_accessanalyzer.types.substring

        return {
            "substring": capo_accessanalyzer.types.substring.serialize_json(
                value["substring"]
            )
        }
    elif "value" in value:
        return {"value": value["value"]}
    else:
        raise SerializationError("PathElement: no variant present")


def deserialize_json(data: dict) -> PathElement:
    if data.get("index") is not None:
        return {"index": data["index"]}
    elif data.get("key") is not None:
        return {"key": data["key"]}
    elif data.get("substring") is not None:
        import capo_accessanalyzer.types.substring

        return {
            "substring": capo_accessanalyzer.types.substring.deserialize_json(
                data["substring"]
            )
        }
    elif data.get("value") is not None:
        return {"value": data["value"]}
    else:
        raise DeserializationError("PathElement: no recognized variant key")

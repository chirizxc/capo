"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextResourceTag``."""

from typing_extensions import TypedDict

from capo_wellarchitected.errors import DeserializationError


class ContextResourceTag(TypedDict, closed=True):
    key: "str"
    """<p>The tag key.</p>"""
    value: "str"
    """<p>The tag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextResourceTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ContextResourceTag:
    out: ContextResourceTag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ContextResourceTag.key required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("ContextResourceTag.value required")
    return out

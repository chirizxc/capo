"""Generated from Smithy shape ``com.amazonaws.quicksight#UserLimitsEntry``."""

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError


class UserLimitsEntry(TypedDict, closed=True):
    user_name: "str"
    """<p>The name of the user.</p>"""
    namespace: "str"
    """<p>The namespace of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserLimitsEntry) -> dict:
    out: dict = {}
    out["userName"] = value["user_name"]
    out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> UserLimitsEntry:
    out: UserLimitsEntry = {}  # type: ignore[typeddict-item]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    else:
        raise DeserializationError("UserLimitsEntry.user_name required")
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("UserLimitsEntry.namespace required")
    return out

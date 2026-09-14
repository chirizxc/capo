"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryError``."""

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError


class ProtectedQueryError(TypedDict, closed=True):
    message: "str"
    """<p>A description of why the query failed.</p>"""
    code: "str"
    """<p>An error code for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ProtectedQueryError:
    out: ProtectedQueryError = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ProtectedQueryError.message required")
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ProtectedQueryError.code required")
    return out

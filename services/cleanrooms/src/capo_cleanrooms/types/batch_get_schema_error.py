"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.table_alias


class BatchGetSchemaError(TypedDict, closed=True):
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>An error name for the error.</p>"""
    code: "str"
    """<p>An error code for the error. </p>"""
    message: "str"
    """<p>An error message for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaError) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetSchemaError:
    out: BatchGetSchemaError = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BatchGetSchemaError.name required")
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchGetSchemaError.code required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchGetSchemaError.message required")
    return out

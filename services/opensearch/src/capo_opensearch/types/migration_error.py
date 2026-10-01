"""Generated from Smithy shape ``com.amazonaws.opensearch#MigrationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.string


class MigrationError(TypedDict, closed=True):
    code: NotRequired["capo_opensearch.types.string.String"]
    """<p>The error code identifying the type of failure.</p>"""
    message: NotRequired["capo_opensearch.types.string.String"]
    """<p>A human-readable description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationError) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MigrationError:
    out: MigrationError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out

"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCauseEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_boolean
    import capo_xray.types.nullable_double
    import capo_xray.types.string


class ResponseTimeRootCauseEntity(TypedDict, closed=True):
    name: NotRequired["capo_xray.types.string.String"]
    """<p>The name of the entity.</p>"""
    coverage: NotRequired["capo_xray.types.nullable_double.NullableDouble"]
    """<p>The type and messages of the exceptions.</p>"""
    remote: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>A flag that denotes a remote subsegment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCauseEntity) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "coverage" in value:
        out["Coverage"] = (
            "NaN"
            if value["coverage"] != value["coverage"]
            else "Infinity"
            if value["coverage"] == float("inf")
            else "-Infinity"
            if value["coverage"] == float("-inf")
            else value["coverage"]
        )
    if "remote" in value:
        out["Remote"] = value["remote"]
    return out


def deserialize_json(data: dict) -> ResponseTimeRootCauseEntity:
    out: ResponseTimeRootCauseEntity = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Coverage") is not None:
        out["coverage"] = float(data["Coverage"])
    if data.get("Remote") is not None:
        out["remote"] = data["Remote"]
    return out

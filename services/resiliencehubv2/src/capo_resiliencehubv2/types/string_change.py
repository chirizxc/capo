"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StringChange``."""

from typing_extensions import NotRequired, TypedDict


class StringChange(TypedDict, closed=True):
    old_value: NotRequired["str"]
    """<p>The old value.</p>"""
    new_value: NotRequired["str"]
    """<p>The new value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringChange) -> dict:
    out: dict = {}
    if "old_value" in value:
        out["oldValue"] = value["old_value"]
    if "new_value" in value:
        out["newValue"] = value["new_value"]
    return out


def deserialize_json(data: dict) -> StringChange:
    out: StringChange = {}  # type: ignore[typeddict-item]
    if data.get("oldValue") is not None:
        out["old_value"] = data["oldValue"]
    if data.get("newValue") is not None:
        out["new_value"] = data["newValue"]
    return out

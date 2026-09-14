"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#SuggestedFix``."""

from typing_extensions import NotRequired, TypedDict


class SuggestedFix(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>A description of the suggested code fix and why it is being suggested. </p>"""
    code: NotRequired["str"]
    """<p>The suggested code fix. If applicable, includes code patch to replace your source code. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedFix) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> SuggestedFix:
    out: SuggestedFix = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    return out

"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssertionDeletedMetadata``."""

from typing_extensions import NotRequired, TypedDict


class AssertionDeletedMetadata(TypedDict, closed=True):
    assertion_id: NotRequired["str"]
    """<p>The unique identifier of the deleted assertion.</p>"""
    assertion_name: NotRequired["str"]
    """<p>The name of the deleted assertion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssertionDeletedMetadata) -> dict:
    out: dict = {}
    if "assertion_id" in value:
        out["assertionId"] = value["assertion_id"]
    if "assertion_name" in value:
        out["assertionName"] = value["assertion_name"]
    return out


def deserialize_json(data: dict) -> AssertionDeletedMetadata:
    out: AssertionDeletedMetadata = {}  # type: ignore[typeddict-item]
    if data.get("assertionId") is not None:
        out["assertion_id"] = data["assertionId"]
    if data.get("assertionName") is not None:
        out["assertion_name"] = data["assertionName"]
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluationAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.string


class ContactEvaluationAttributeValue(TypedDict, closed=True):
    string_value: NotRequired["capo_connect.types.string.String"]
    """<p>A string value for the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactEvaluationAttributeValue) -> dict:
    out: dict = {}
    if "string_value" in value:
        out["StringValue"] = value["string_value"]
    return out


def deserialize_json(data: dict) -> ContactEvaluationAttributeValue:
    out: ContactEvaluationAttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("StringValue") is not None:
        out["string_value"] = data["StringValue"]
    return out

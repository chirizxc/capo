"""Generated from Smithy shape ``com.amazonaws.guardduty#ModelDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class ModelDetail(TypedDict, closed=True):
    model_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The identifier of the AI model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelDetail) -> dict:
    out: dict = {}
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> ModelDetail:
    out: ModelDetail = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    return out

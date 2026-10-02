"""Generated from Smithy shape ``com.amazonaws.guardduty#ModelDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.model_detail

ModelDetails: TypeAlias = list["capo_guardduty.types.model_detail.ModelDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelDetails) -> list:
    import capo_guardduty.types.model_detail

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.model_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelDetails:
    import capo_guardduty.types.model_detail

    out: ModelDetails = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.model_detail.deserialize_json(item))
    return out

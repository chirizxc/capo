"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormValidationFindingItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_validation_finding_item_property
    import capo_connect.types.reference_id


class EvaluationFormValidationFindingItem(TypedDict, closed=True):
    ref_id: NotRequired["capo_connect.types.reference_id.ReferenceId"]
    """<p>The identifier of the evaluation form item (question or section) affected by the finding.</p>"""
    property: NotRequired[
        "capo_connect.types.evaluation_form_validation_finding_item_property.EvaluationFormValidationFindingItemProperty"
    ]
    """<p>The specific property of the evaluation form item that the finding relates to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormValidationFindingItem) -> dict:
    out: dict = {}
    if "ref_id" in value:
        out["RefId"] = value["ref_id"]
    if "property" in value:
        out["Property"] = value["property"]
    return out


def deserialize_json(data: dict) -> EvaluationFormValidationFindingItem:
    out: EvaluationFormValidationFindingItem = {}  # type: ignore[typeddict-item]
    if data.get("RefId") is not None:
        out["ref_id"] = data["RefId"]
    if data.get("Property") is not None:
        out["property"] = data["Property"]
    return out

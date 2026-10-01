"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AssessmentTargetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_id


class AssessmentTargetSummary(TypedDict, closed=True):
    entity_id: NotRequired["capo_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>The unique ID of the entity that was assessed.</p>"""
    change_set_id: NotRequired["capo_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>The unique ID of the change set that was assessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentTargetSummary) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "change_set_id" in value:
        out["ChangeSetId"] = value["change_set_id"]
    return out


def deserialize_json(data: dict) -> AssessmentTargetSummary:
    out: AssessmentTargetSummary = {}  # type: ignore[typeddict-item]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("ChangeSetId") is not None:
        out["change_set_id"] = data["ChangeSetId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AssessmentTargetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_id


class AssessmentTargetFilter(TypedDict, closed=True):
    entity_id: NotRequired["capo_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>The unique ID of the entity whose assessments you want to list.</p>"""
    change_set_id: NotRequired["capo_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>The unique ID of the change set that triggered the assessments you want to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentTargetFilter) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "change_set_id" in value:
        out["ChangeSetId"] = value["change_set_id"]
    return out


def deserialize_json(data: dict) -> AssessmentTargetFilter:
    out: AssessmentTargetFilter = {}  # type: ignore[typeddict-item]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("ChangeSetId") is not None:
        out["change_set_id"] = data["ChangeSetId"]
    return out

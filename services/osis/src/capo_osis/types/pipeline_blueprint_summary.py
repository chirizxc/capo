"""Generated from Smithy shape ``com.amazonaws.osis#PipelineBlueprintSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.string


class PipelineBlueprintSummary(TypedDict, closed=True):
    blueprint_name: NotRequired["capo_osis.types.string.String"]
    """<p>The name of the blueprint.</p>"""
    display_name: NotRequired["capo_osis.types.string.String"]
    """<p>The display name of the blueprint.</p>"""
    display_description: NotRequired["capo_osis.types.string.String"]
    """<p>A description of the blueprint.</p>"""
    service: NotRequired["capo_osis.types.string.String"]
    """<p>The name of the service that the blueprint is associated with.</p>"""
    use_case: NotRequired["capo_osis.types.string.String"]
    """<p>The use case that the blueprint relates to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineBlueprintSummary) -> dict:
    out: dict = {}
    if "blueprint_name" in value:
        out["BlueprintName"] = value["blueprint_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "display_description" in value:
        out["DisplayDescription"] = value["display_description"]
    if "service" in value:
        out["Service"] = value["service"]
    if "use_case" in value:
        out["UseCase"] = value["use_case"]
    return out


def deserialize_json(data: dict) -> PipelineBlueprintSummary:
    out: PipelineBlueprintSummary = {}  # type: ignore[typeddict-item]
    if data.get("BlueprintName") is not None:
        out["blueprint_name"] = data["BlueprintName"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("DisplayDescription") is not None:
        out["display_description"] = data["DisplayDescription"]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    if data.get("UseCase") is not None:
        out["use_case"] = data["UseCase"]
    return out

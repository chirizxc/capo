"""Generated from Smithy shape ``com.amazonaws.controlcatalog#AssociatedObjectiveSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.objective_arn


class AssociatedObjectiveSummary(TypedDict, closed=True):
    arn: NotRequired["capo_controlcatalog.types.objective_arn.ObjectiveArn"]
    """<p>The Amazon Resource Name (ARN) of the related objective.</p>"""
    name: NotRequired["str"]
    """<p>The name of the related objective.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedObjectiveSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssociatedObjectiveSummary:
    out: AssociatedObjectiveSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out

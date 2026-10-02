"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateInvestigationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_id


class CreateInvestigationResponse(TypedDict, closed=True):
    investigation_id: NotRequired[
        "capo_guardduty.types.investigation_id.InvestigationId"
    ]
    """<p>The unique identifier of the newly created investigation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInvestigationResponse) -> dict:
    out: dict = {}
    if "investigation_id" in value:
        out["investigationId"] = value["investigation_id"]
    return out


def deserialize_json(data: dict) -> CreateInvestigationResponse:
    out: CreateInvestigationResponse = {}  # type: ignore[typeddict-item]
    if data.get("investigationId") is not None:
        out["investigation_id"] = data["investigationId"]
    return out

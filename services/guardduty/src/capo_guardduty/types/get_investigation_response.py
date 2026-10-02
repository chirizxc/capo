"""Generated from Smithy shape ``com.amazonaws.guardduty#GetInvestigationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation


class GetInvestigationResponse(TypedDict, closed=True):
    investigation: NotRequired["capo_guardduty.types.investigation.Investigation"]
    """<p>The details and results of the requested investigation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationResponse) -> dict:
    out: dict = {}
    if "investigation" in value:
        import capo_guardduty.types.investigation

        out["investigation"] = capo_guardduty.types.investigation.serialize_json(
            value["investigation"]
        )
    return out


def deserialize_json(data: dict) -> GetInvestigationResponse:
    out: GetInvestigationResponse = {}  # type: ignore[typeddict-item]
    if data.get("investigation") is not None:
        import capo_guardduty.types.investigation

        out["investigation"] = capo_guardduty.types.investigation.deserialize_json(
            data["investigation"]
        )
    return out

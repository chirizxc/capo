"""Generated from Smithy shape ``com.amazonaws.guardduty#ListInvestigationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_summaries
    import capo_guardduty.types.next_token


class ListInvestigationsResponse(TypedDict, closed=True):
    investigations: NotRequired[
        "capo_guardduty.types.investigation_summaries.InvestigationSummaries"
    ]
    """<p>A list of investigation summaries associated with the specified detector.</p>"""
    next_token: NotRequired["capo_guardduty.types.next_token.NextToken"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationsResponse) -> dict:
    out: dict = {}
    if "investigations" in value:
        import capo_guardduty.types.investigation_summaries

        out["investigations"] = (
            capo_guardduty.types.investigation_summaries.serialize_json(
                value["investigations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvestigationsResponse:
    out: ListInvestigationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("investigations") is not None:
        import capo_guardduty.types.investigation_summaries

        out["investigations"] = (
            capo_guardduty.types.investigation_summaries.deserialize_json(
                data["investigations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

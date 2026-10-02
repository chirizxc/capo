"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListAssessmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.assessment_summary_list
    import capo_marketplace_catalog.types.next_token


class ListAssessmentsResponse(TypedDict, closed=True):
    assessment_summary_list: NotRequired[
        "capo_marketplace_catalog.types.assessment_summary_list.AssessmentSummaryList"
    ]
    """<p>An array of <code>AssessmentSummary</code> objects.</p>"""
    next_token: NotRequired["capo_marketplace_catalog.types.next_token.NextToken"]
    """<p>The value of the next token, if it exists. <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentsResponse) -> dict:
    out: dict = {}
    if "assessment_summary_list" in value:
        import capo_marketplace_catalog.types.assessment_summary_list

        out["AssessmentSummaryList"] = (
            capo_marketplace_catalog.types.assessment_summary_list.serialize_json(
                value["assessment_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssessmentsResponse:
    out: ListAssessmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AssessmentSummaryList") is not None:
        import capo_marketplace_catalog.types.assessment_summary_list

        out["assessment_summary_list"] = (
            capo_marketplace_catalog.types.assessment_summary_list.deserialize_json(
                data["AssessmentSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

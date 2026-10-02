"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRunResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description


class ExperimentRunResult(TypedDict, closed=True):
    executive_summary: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A summary of the experiment outcome and key findings.</p>"""
    reasons_to_launch: NotRequired["capo_appconfig.types.description.Description"]
    """<p>Evidence in favor of launching the winning treatment.</p>"""
    reasons_not_to_launch: NotRequired["capo_appconfig.types.description.Description"]
    """<p>Evidence against launching the treatment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRunResult) -> dict:
    out: dict = {}
    if "executive_summary" in value:
        out["ExecutiveSummary"] = value["executive_summary"]
    if "reasons_to_launch" in value:
        out["ReasonsToLaunch"] = value["reasons_to_launch"]
    if "reasons_not_to_launch" in value:
        out["ReasonsNotToLaunch"] = value["reasons_not_to_launch"]
    return out


def deserialize_json(data: dict) -> ExperimentRunResult:
    out: ExperimentRunResult = {}  # type: ignore[typeddict-item]
    if data.get("ExecutiveSummary") is not None:
        out["executive_summary"] = data["ExecutiveSummary"]
    if data.get("ReasonsToLaunch") is not None:
        out["reasons_to_launch"] = data["ReasonsToLaunch"]
    if data.get("ReasonsNotToLaunch") is not None:
        out["reasons_not_to_launch"] = data["ReasonsNotToLaunch"]
    return out

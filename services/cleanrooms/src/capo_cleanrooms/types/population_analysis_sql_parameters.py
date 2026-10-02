"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulationAnalysisSqlParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_arn


class PopulationAnalysisSqlParameters(TypedDict, closed=True):
    query_string: NotRequired["str"]
    """<p>The SQL query string used to populate the intermediate table.</p>"""
    analysis_template_arn: NotRequired[
        "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the analysis template to use for populating the intermediate table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PopulationAnalysisSqlParameters) -> dict:
    out: dict = {}
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "analysis_template_arn" in value:
        out["analysisTemplateArn"] = value["analysis_template_arn"]
    return out


def deserialize_json(data: dict) -> PopulationAnalysisSqlParameters:
    out: PopulationAnalysisSqlParameters = {}  # type: ignore[typeddict-item]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    if data.get("analysisTemplateArn") is not None:
        out["analysis_template_arn"] = data["analysisTemplateArn"]
    return out

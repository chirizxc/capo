"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIntermediateTableAnalysisRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_analysis_rule


class UpdateIntermediateTableAnalysisRuleOutput(TypedDict, closed=True):
    analysis_rule: "capo_cleanrooms.types.intermediate_table_analysis_rule.IntermediateTableAnalysisRule"
    """<p>The updated analysis rule for the intermediate table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntermediateTableAnalysisRuleOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.intermediate_table_analysis_rule

    out["analysisRule"] = (
        capo_cleanrooms.types.intermediate_table_analysis_rule.serialize_json(
            value["analysis_rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIntermediateTableAnalysisRuleOutput:
    out: UpdateIntermediateTableAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("analysisRule") is not None:
        import capo_cleanrooms.types.intermediate_table_analysis_rule

        out["analysis_rule"] = (
            capo_cleanrooms.types.intermediate_table_analysis_rule.deserialize_json(
                data["analysisRule"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIntermediateTableAnalysisRuleOutput.analysis_rule required"
        )
    return out

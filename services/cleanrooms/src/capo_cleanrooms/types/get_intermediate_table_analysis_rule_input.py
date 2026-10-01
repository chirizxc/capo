"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetIntermediateTableAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.membership_identifier


class GetIntermediateTableAnalysisRuleInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""
    intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table for which to retrieve the analysis rule.</p>"""
    analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType"
    """<p>The type of analysis rule to retrieve. Currently, only <code>CUSTOM</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntermediateTableAnalysisRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntermediateTableAnalysisRuleInput:
    out: GetIntermediateTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    return out

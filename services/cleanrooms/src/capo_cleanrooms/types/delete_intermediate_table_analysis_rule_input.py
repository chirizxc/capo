"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteIntermediateTableAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.membership_identifier


class DeleteIntermediateTableAnalysisRuleInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""
    intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table from which to delete the analysis rule.</p>"""
    analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType"
    """<p>The type of analysis rule to delete. Currently, only <code>CUSTOM</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntermediateTableAnalysisRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntermediateTableAnalysisRuleInput:
    out: DeleteIntermediateTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    return out

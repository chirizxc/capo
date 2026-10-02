"""Generated from Smithy shape ``com.amazonaws.guardduty#RuleDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.rule_expression


class RuleDefinition(TypedDict, closed=True):
    expression: NotRequired["capo_guardduty.types.rule_expression.RuleExpression"]
    """<p>The detection logic expression for the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleDefinition) -> dict:
    out: dict = {}
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> RuleDefinition:
    out: RuleDefinition = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    return out

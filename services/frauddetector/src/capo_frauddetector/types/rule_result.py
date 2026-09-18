"""Generated from Smithy shape ``com.amazonaws.frauddetector#RuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.list_of_strings
    import capo_frauddetector.types.string


class RuleResult(TypedDict, closed=True):
    rule_id: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The rule ID that was matched, based on the rule execution mode.</p>"""
    outcomes: NotRequired["capo_frauddetector.types.list_of_strings.ListOfStrings"]
    """<p>The outcomes of the matched rule, based on the rule execution mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleResult) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "outcomes" in value:
        import capo_frauddetector.types.list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
                value["outcomes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleResult:
    out: RuleResult = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("outcomes") is not None:
        import capo_frauddetector.types.list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    return out

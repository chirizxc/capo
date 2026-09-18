"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedAutomationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class UnprocessedAutomationRule(TypedDict, closed=True):
    rule_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) for the unprocessed automation rule. </p>"""
    error_code: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The error code associated with the unprocessed automation rule. </p>"""
    error_message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> An error message describing why a request didn't process a specific rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedAutomationRule) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> UnprocessedAutomationRule:
    out: UnprocessedAutomationRule = {}  # type: ignore[typeddict-item]
    if data.get("RuleArn") is not None:
        out["rule_arn"] = data["RuleArn"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out

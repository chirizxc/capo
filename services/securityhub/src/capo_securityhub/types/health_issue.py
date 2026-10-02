"""Generated from Smithy shape ``com.amazonaws.securityhub#HealthIssue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.health_issue_code
    import capo_securityhub.types.non_empty_string


class HealthIssue(TypedDict, closed=True):
    code: NotRequired["capo_securityhub.types.health_issue_code.HealthIssueCode"]
    """<p>The error code that identifies the type of health issue.</p>"""
    message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A human-readable message that describes the health issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthIssue) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_securityhub.types.health_issue_code

        out["Code"] = capo_securityhub.types.health_issue_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> HealthIssue:
    out: HealthIssue = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_securityhub.types.health_issue_code

        out["code"] = capo_securityhub.types.health_issue_code.deserialize_json(
            data["Code"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out

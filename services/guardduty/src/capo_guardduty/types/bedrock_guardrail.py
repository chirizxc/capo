"""Generated from Smithy shape ``com.amazonaws.guardduty#BedrockGuardrail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class BedrockGuardrail(TypedDict, closed=True):
    arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ARN of the Bedrock guardrail.</p>"""
    version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the Bedrock guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockGuardrail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> BedrockGuardrail:
    out: BedrockGuardrail = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out

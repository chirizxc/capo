"""Generated from Smithy shape ``com.amazonaws.guardduty#ContentPolicyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.confidence_level
    import capo_guardduty.types.content_policy_filter_action
    import capo_guardduty.types.content_policy_filter_type


class ContentPolicyFilter(TypedDict, closed=True):
    type: NotRequired[
        "capo_guardduty.types.content_policy_filter_type.ContentPolicyFilterType"
    ]
    """<p>The type of content that was filtered by the guardrail.</p>"""
    confidence: NotRequired["capo_guardduty.types.confidence_level.ConfidenceLevel"]
    """<p>The confidence level that the content matched the filter.</p>"""
    action: NotRequired[
        "capo_guardduty.types.content_policy_filter_action.ContentPolicyFilterAction"
    ]
    """<p>The action taken by the guardrail filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentPolicyFilter) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_guardduty.types.content_policy_filter_type

        out["type"] = capo_guardduty.types.content_policy_filter_type.serialize_json(
            value["type"]
        )
    if "confidence" in value:
        import capo_guardduty.types.confidence_level

        out["confidence"] = capo_guardduty.types.confidence_level.serialize_json(
            value["confidence"]
        )
    if "action" in value:
        import capo_guardduty.types.content_policy_filter_action

        out["action"] = (
            capo_guardduty.types.content_policy_filter_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentPolicyFilter:
    out: ContentPolicyFilter = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_guardduty.types.content_policy_filter_type

        out["type"] = capo_guardduty.types.content_policy_filter_type.deserialize_json(
            data["type"]
        )
    if data.get("confidence") is not None:
        import capo_guardduty.types.confidence_level

        out["confidence"] = capo_guardduty.types.confidence_level.deserialize_json(
            data["confidence"]
        )
    if data.get("action") is not None:
        import capo_guardduty.types.content_policy_filter_action

        out["action"] = (
            capo_guardduty.types.content_policy_filter_action.deserialize_json(
                data["action"]
            )
        )
    return out

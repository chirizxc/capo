"""Generated from Smithy shape ``com.amazonaws.guardduty#BedrockGuardrailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.bedrock_guardrails
    import capo_guardduty.types.content_policy_filters
    import capo_guardduty.types.guardrail_action
    import capo_guardduty.types.guardrail_source
    import capo_guardduty.types.string


class BedrockGuardrailDetails(TypedDict, closed=True):
    guardrail_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ARN of the Bedrock guardrail. This field is deprecated. Use the <code>guardrails</code> list instead.</p>"""
    guardrail_version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the Bedrock guardrail. This field is deprecated. Use the <code>guardrails</code> list instead.</p>"""
    guardrails: NotRequired["capo_guardduty.types.bedrock_guardrails.BedrockGuardrails"]
    """<p>The list of Bedrock guardrails associated with the finding.</p>"""
    guardrail_action: NotRequired[
        "capo_guardduty.types.guardrail_action.GuardrailAction"
    ]
    """<p>Indicates whether the guardrail intervened or not.</p>"""
    guardrail_source: NotRequired[
        "capo_guardduty.types.guardrail_source.GuardrailSource"
    ]
    """<p>Indicates whether the guardrail was applied on the input or output of the model invocation.</p>"""
    content_policy_filters: NotRequired[
        "capo_guardduty.types.content_policy_filters.ContentPolicyFilters"
    ]
    """<p>The list of content policy filters that matched during the guardrail evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockGuardrailDetails) -> dict:
    out: dict = {}
    if "guardrail_arn" in value:
        out["guardrailArn"] = value["guardrail_arn"]
    if "guardrail_version" in value:
        out["guardrailVersion"] = value["guardrail_version"]
    if "guardrails" in value:
        import capo_guardduty.types.bedrock_guardrails

        out["guardrails"] = capo_guardduty.types.bedrock_guardrails.serialize_json(
            value["guardrails"]
        )
    if "guardrail_action" in value:
        import capo_guardduty.types.guardrail_action

        out["guardrailAction"] = capo_guardduty.types.guardrail_action.serialize_json(
            value["guardrail_action"]
        )
    if "guardrail_source" in value:
        import capo_guardduty.types.guardrail_source

        out["guardrailSource"] = capo_guardduty.types.guardrail_source.serialize_json(
            value["guardrail_source"]
        )
    if "content_policy_filters" in value:
        import capo_guardduty.types.content_policy_filters

        out["contentPolicyFilters"] = (
            capo_guardduty.types.content_policy_filters.serialize_json(
                value["content_policy_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> BedrockGuardrailDetails:
    out: BedrockGuardrailDetails = {}  # type: ignore[typeddict-item]
    if data.get("guardrailArn") is not None:
        out["guardrail_arn"] = data["guardrailArn"]
    if data.get("guardrailVersion") is not None:
        out["guardrail_version"] = data["guardrailVersion"]
    if data.get("guardrails") is not None:
        import capo_guardduty.types.bedrock_guardrails

        out["guardrails"] = capo_guardduty.types.bedrock_guardrails.deserialize_json(
            data["guardrails"]
        )
    if data.get("guardrailAction") is not None:
        import capo_guardduty.types.guardrail_action

        out["guardrail_action"] = (
            capo_guardduty.types.guardrail_action.deserialize_json(
                data["guardrailAction"]
            )
        )
    if data.get("guardrailSource") is not None:
        import capo_guardduty.types.guardrail_source

        out["guardrail_source"] = (
            capo_guardduty.types.guardrail_source.deserialize_json(
                data["guardrailSource"]
            )
        )
    if data.get("contentPolicyFilters") is not None:
        import capo_guardduty.types.content_policy_filters

        out["content_policy_filters"] = (
            capo_guardduty.types.content_policy_filters.deserialize_json(
                data["contentPolicyFilters"]
            )
        )
    return out

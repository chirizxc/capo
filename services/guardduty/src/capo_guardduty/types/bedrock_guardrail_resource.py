"""Generated from Smithy shape ``com.amazonaws.guardduty#BedrockGuardrailResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.guardrail_action
    import capo_guardduty.types.guardrail_source
    import capo_guardduty.types.string


class BedrockGuardrailResource(TypedDict, closed=True):
    version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the Amazon Bedrock guardrail. Valid values are a numeric version, <code>DRAFT</code>, or <code>ENFORCED</code>.</p>"""
    guardrail_action: NotRequired[
        "capo_guardduty.types.guardrail_action.GuardrailAction"
    ]
    """<p>Indicates whether the guardrail intervened during the model invocation.</p>"""
    guardrail_source: NotRequired[
        "capo_guardduty.types.guardrail_source.GuardrailSource"
    ]
    """<p>Indicates whether the guardrail was applied on the input or output of the model invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockGuardrailResource) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
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
    return out


def deserialize_json(data: dict) -> BedrockGuardrailResource:
    out: BedrockGuardrailResource = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
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
    return out

"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanGuardrailAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_action
    import capo_qconnect.types.guardrail_policy_result_list
    import capo_qconnect.types.guardrail_source
    import capo_qconnect.types.non_empty_string


class SpanGuardrailAssessment(TypedDict, closed=True):
    guardrail_id: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>Unique AI Guardrail identifier.</p>"""
    guardrail_name: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>Customer-defined display name of the AI Guardrail resource.</p>"""
    source: "capo_qconnect.types.guardrail_source.GuardrailSource"
    """<p>Content source the guardrail was evaluated against.</p>"""
    action: "capo_qconnect.types.guardrail_action.GuardrailAction"
    """<p>Outcome of the guardrail assessment.</p>"""
    policies: NotRequired[
        "capo_qconnect.types.guardrail_policy_result_list.GuardrailPolicyResultList"
    ]
    """<p>Per-policy assessment results. Absent or empty when action is NONE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanGuardrailAssessment) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailName"] = value["guardrail_name"]
    out["source"] = value["source"]
    out["action"] = value["action"]
    if "policies" in value:
        import capo_qconnect.types.guardrail_policy_result_list

        out["policies"] = (
            capo_qconnect.types.guardrail_policy_result_list.serialize_json(
                value["policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> SpanGuardrailAssessment:
    out: SpanGuardrailAssessment = {}  # type: ignore[typeddict-item]
    if data.get("guardrailId") is not None:
        out["guardrail_id"] = data["guardrailId"]
    else:
        raise DeserializationError("SpanGuardrailAssessment.guardrail_id required")
    if data.get("guardrailName") is not None:
        out["guardrail_name"] = data["guardrailName"]
    else:
        raise DeserializationError("SpanGuardrailAssessment.guardrail_name required")
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("SpanGuardrailAssessment.source required")
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        raise DeserializationError("SpanGuardrailAssessment.action required")
    if data.get("policies") is not None:
        import capo_qconnect.types.guardrail_policy_result_list

        out["policies"] = (
            capo_qconnect.types.guardrail_policy_result_list.deserialize_json(
                data["policies"]
            )
        )
    return out

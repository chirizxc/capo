"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeGuardrailChecksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_results
    import capo_bedrock_runtime.types.guardrail_checks_usage_results


class InvokeGuardrailChecksResponse(TypedDict, closed=True):
    results: (
        "capo_bedrock_runtime.types.guardrail_checks_results.GuardrailChecksResults"
    )
    """<p>The per-check results containing findings from the guardrail evaluation.</p>"""
    usage: "capo_bedrock_runtime.types.guardrail_checks_usage_results.GuardrailChecksUsageResults"
    """<p>The per-check text unit consumption for the guardrail evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeGuardrailChecksResponse) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_results

    out["results"] = capo_bedrock_runtime.types.guardrail_checks_results.serialize_json(
        value["results"]
    )
    import capo_bedrock_runtime.types.guardrail_checks_usage_results

    out["usage"] = (
        capo_bedrock_runtime.types.guardrail_checks_usage_results.serialize_json(
            value["usage"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvokeGuardrailChecksResponse:
    out: InvokeGuardrailChecksResponse = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_results

        out["results"] = (
            capo_bedrock_runtime.types.guardrail_checks_results.deserialize_json(
                data["results"]
            )
        )
    else:
        raise DeserializationError("InvokeGuardrailChecksResponse.results required")
    if data.get("usage") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_usage_results

        out["usage"] = (
            capo_bedrock_runtime.types.guardrail_checks_usage_results.deserialize_json(
                data["usage"]
            )
        )
    else:
        raise DeserializationError("InvokeGuardrailChecksResponse.usage required")
    return out

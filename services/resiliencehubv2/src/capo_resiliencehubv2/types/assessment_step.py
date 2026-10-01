"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentStep``."""

from typing import Literal, TypeAlias, cast

AssessmentStep: TypeAlias = Literal[
    "TOPOLOGY_GENERATION",
    "INPUT_VALIDATION",
    "DESIGN_ANALYSIS",
    "TOPOLOGY_ENHANCEMENT",
    "SERVICE_FUNCTION_GENERATION",
    "POLICY_VALIDATION",
    "RESILIENCE_ASSESSMENT",
    "FAILURE_MODE_FINDINGS_CONSOLIDATION",
    "FAILURE_MODE_FINDINGS_ENRICHMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentStep) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStep:
    return cast(AssessmentStep, data)

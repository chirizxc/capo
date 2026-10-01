"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightsFailureCategory``."""

from typing import Literal, TypeAlias, cast

"""Failure category taxonomy for agent session insights. Values must stay in sync with the category registry in AgentCoreLens (amzn_agentcore_lens.config.failure_detection.FAILURE_CATEGORIES)."""
InsightsFailureCategory: TypeAlias = Literal[
    "execution-error-category-authentication",
    "execution-error-category-resource-not-found",
    "execution-error-category-service-errors",
    "execution-error-category-rate-limiting",
    "execution-error-category-formatting",
    "execution-error-category-timeout",
    "execution-error-category-resource-exhaustion",
    "execution-error-category-environment",
    "execution-error-category-tool-schema",
    "task-instruction-category-non-compliance",
    "task-instruction-category-problem-id",
    "incorrect-actions-category-tool-selection",
    "incorrect-actions-category-poor-information-retrieval",
    "incorrect-actions-category-clarification",
    "incorrect-actions-category-inappropriate-info-request",
    "context-handling-error-category-context-handling-failures",
    "hallucination-category-hall-capabilities",
    "hallucination-category-hall-misunderstand",
    "hallucination-category-hall-usage",
    "hallucination-category-hall-history",
    "hallucination-category-hall-params",
    "hallucination-category-fabricate-tool-outputs",
    "repetitive-behavior-category-repetition-tool",
    "repetitive-behavior-category-repetition-info",
    "repetitive-behavior-category-step-repetition",
    "orchestration-related-errors-category-reasoning-mismatch",
    "orchestration-related-errors-category-goal-deviation",
    "orchestration-related-errors-category-premature-termination",
    "orchestration-related-errors-category-unaware-termination",
    "llm-output-category-nonsensical",
    "configuration-mismatch-category-tool-definition",
    "coding-use-case-specific-failure-types-category-edge-case-oversights",
    "coding-use-case-specific-failure-types-category-dependency-issues",
    "other",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightsFailureCategory) -> str:
    return value


def deserialize_json(data: str) -> InsightsFailureCategory:
    return cast(InsightsFailureCategory, data)

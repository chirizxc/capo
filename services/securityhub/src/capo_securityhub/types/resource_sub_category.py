"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceSubCategory``."""

from typing import Literal, TypeAlias, cast

ResourceSubCategory: TypeAlias = Literal[
    "Model",
    "ModelServing",
    "Agent",
    "AgentFramework",
    "AgentToolsAndIdentity",
    "SafetyAndGuardrail",
    "KnowledgeAndData",
    "OrchestrationAndPipeline",
    "ExternalEndpoint",
    "Development",
    "Other",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSubCategory) -> str:
    return value


def deserialize_json(data: str) -> ResourceSubCategory:
    return cast(ResourceSubCategory, data)

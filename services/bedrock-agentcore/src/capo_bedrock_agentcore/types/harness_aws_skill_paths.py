"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessAwsSkillPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_aws_skill_path

HarnessAwsSkillPaths: TypeAlias = list[
    "capo_bedrock_agentcore.types.harness_aws_skill_path.HarnessAwsSkillPath"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAwsSkillPaths) -> list:
    return list(value)


def deserialize_json(data: list) -> HarnessAwsSkillPaths:
    return [item for item in data if item is not None]

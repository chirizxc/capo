"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSkillAwsSkillsSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_aws_skill_paths


class HarnessSkillAwsSkillsSource(TypedDict, closed=True):
    paths: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_aws_skill_paths.HarnessAwsSkillPaths"
    ]
    """<p>Optionally filter allowed skills with glob syntax, e.g., ['core-skills/*'].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkillAwsSkillsSource) -> dict:
    out: dict = {}
    if "paths" in value:
        import capo_bedrock_agentcore_control.types.harness_aws_skill_paths

        out["paths"] = (
            capo_bedrock_agentcore_control.types.harness_aws_skill_paths.serialize_json(
                value["paths"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessSkillAwsSkillsSource:
    out: HarnessSkillAwsSkillsSource = {}  # type: ignore[typeddict-item]
    if data.get("paths") is not None:
        import capo_bedrock_agentcore_control.types.harness_aws_skill_paths

        out["paths"] = (
            capo_bedrock_agentcore_control.types.harness_aws_skill_paths.deserialize_json(
                data["paths"]
            )
        )
    return out

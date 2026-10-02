"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.target

AutomationTargets: TypeAlias = list["capo_ssm.types.target.Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationTargets) -> list:
    import capo_ssm.types.target

    out: list = []
    for item in value:
        out.append(capo_ssm.types.target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AutomationTargets:
    import capo_ssm.types.target

    out: AutomationTargets = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.target.deserialize_aws_json_1_1(item))
    return out

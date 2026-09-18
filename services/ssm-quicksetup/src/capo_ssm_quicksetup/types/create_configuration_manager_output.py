"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#CreateConfigurationManagerOutput``."""

from typing_extensions import TypedDict

from capo_ssm_quicksetup.errors import DeserializationError


class CreateConfigurationManagerOutput(TypedDict, closed=True):
    manager_arn: "str"
    """<p>The ARN for the newly created configuration manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationManagerOutput) -> dict:
    out: dict = {}
    out["ManagerArn"] = value["manager_arn"]
    return out


def deserialize_json(data: dict) -> CreateConfigurationManagerOutput:
    out: CreateConfigurationManagerOutput = {}  # type: ignore[typeddict-item]
    if data.get("ManagerArn") is not None:
        out["manager_arn"] = data["ManagerArn"]
    else:
        raise DeserializationError(
            "CreateConfigurationManagerOutput.manager_arn required"
        )
    return out

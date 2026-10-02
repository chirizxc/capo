"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LicenseSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.license_specification

LicenseSpecificationList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.license_specification.LicenseSpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: LicenseSpecificationList) -> list:
    import capo_bedrock_agentcore_control.types.license_specification

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.license_specification.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LicenseSpecificationList:
    import capo_bedrock_agentcore_control.types.license_specification

    out: LicenseSpecificationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.license_specification.deserialize_json(
                item
            )
        )
    return out

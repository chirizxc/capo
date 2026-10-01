"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchCreateSecurityRequirementResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.batch_create_security_requirement_result

BatchCreateSecurityRequirementResultList: TypeAlias = list[
    "capo_securityagent.types.batch_create_security_requirement_result.BatchCreateSecurityRequirementResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateSecurityRequirementResultList) -> list:
    import capo_securityagent.types.batch_create_security_requirement_result

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.batch_create_security_requirement_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateSecurityRequirementResultList:
    import capo_securityagent.types.batch_create_security_requirement_result

    out: BatchCreateSecurityRequirementResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.batch_create_security_requirement_result.deserialize_json(
                item
            )
        )
    return out

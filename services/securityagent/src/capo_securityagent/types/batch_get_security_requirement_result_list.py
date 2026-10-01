"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetSecurityRequirementResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.batch_get_security_requirement_result

BatchGetSecurityRequirementResultList: TypeAlias = list[
    "capo_securityagent.types.batch_get_security_requirement_result.BatchGetSecurityRequirementResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSecurityRequirementResultList) -> list:
    import capo_securityagent.types.batch_get_security_requirement_result

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.batch_get_security_requirement_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetSecurityRequirementResultList:
    import capo_securityagent.types.batch_get_security_requirement_result

    out: BatchGetSecurityRequirementResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.batch_get_security_requirement_result.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchSecurityRequirementErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.batch_security_requirement_error

BatchSecurityRequirementErrors: TypeAlias = list[
    "capo_securityagent.types.batch_security_requirement_error.BatchSecurityRequirementError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchSecurityRequirementErrors) -> list:
    import capo_securityagent.types.batch_security_requirement_error

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.batch_security_requirement_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchSecurityRequirementErrors:
    import capo_securityagent.types.batch_security_requirement_error

    out: BatchSecurityRequirementErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.batch_security_requirement_error.deserialize_json(
                item
            )
        )
    return out

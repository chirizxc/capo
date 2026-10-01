"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_summary

SecurityRequirementSummaryList: TypeAlias = list[
    "capo_securityagent.types.security_requirement_summary.SecurityRequirementSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementSummaryList) -> list:
    import capo_securityagent.types.security_requirement_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.security_requirement_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityRequirementSummaryList:
    import capo_securityagent.types.security_requirement_summary

    out: SecurityRequirementSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.security_requirement_summary.deserialize_json(item)
        )
    return out

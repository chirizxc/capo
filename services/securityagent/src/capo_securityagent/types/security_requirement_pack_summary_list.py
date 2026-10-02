"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementPackSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_pack_summary

SecurityRequirementPackSummaryList: TypeAlias = list[
    "capo_securityagent.types.security_requirement_pack_summary.SecurityRequirementPackSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementPackSummaryList) -> list:
    import capo_securityagent.types.security_requirement_pack_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.security_requirement_pack_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SecurityRequirementPackSummaryList:
    import capo_securityagent.types.security_requirement_pack_summary

    out: SecurityRequirementPackSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.security_requirement_pack_summary.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConsentPortalSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consent_portal_summary

ConsentPortalSummaries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.consent_portal_summary.ConsentPortalSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsentPortalSummaries) -> list:
    import capo_bedrock_agentcore_control.types.consent_portal_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.consent_portal_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConsentPortalSummaries:
    import capo_bedrock_agentcore_control.types.consent_portal_summary

    out: ConsentPortalSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.consent_portal_summary.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConsentPortalSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consent_portal_source

ConsentPortalSources: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.consent_portal_source.ConsentPortalSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsentPortalSources) -> list:
    import capo_bedrock_agentcore_control.types.consent_portal_source

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.consent_portal_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConsentPortalSources:
    import capo_bedrock_agentcore_control.types.consent_portal_source

    out: ConsentPortalSources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.consent_portal_source.deserialize_json(
                item
            )
        )
    return out

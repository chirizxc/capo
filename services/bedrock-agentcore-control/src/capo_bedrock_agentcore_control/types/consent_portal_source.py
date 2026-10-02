"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConsentPortalSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consent_portal_source_identifier_type
    import capo_bedrock_agentcore_control.types.consent_portal_source_type


class ConsentPortalSource(TypedDict, closed=True):
    identifier: "capo_bedrock_agentcore_control.types.consent_portal_source_identifier_type.ConsentPortalSourceIdentifierType"
    """<p>The identifier of the source resource. For an <code>agentcore-gateway</code> source, this is the gateway ID or its Amazon Resource Name (ARN).</p>"""
    type: "capo_bedrock_agentcore_control.types.consent_portal_source_type.ConsentPortalSourceType"
    """<p>The type of the source resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsentPortalSource) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    import capo_bedrock_agentcore_control.types.consent_portal_source_type

    out["type"] = (
        capo_bedrock_agentcore_control.types.consent_portal_source_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConsentPortalSource:
    out: ConsentPortalSource = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("ConsentPortalSource.identifier required")
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_source_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.consent_portal_source_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ConsentPortalSource.type required")
    return out

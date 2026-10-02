"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConsentPortalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.consent_portal_arn_type
    import capo_bedrock_agentcore_control.types.consent_portal_description_type
    import capo_bedrock_agentcore_control.types.consent_portal_id_type
    import capo_bedrock_agentcore_control.types.consent_portal_name_type
    import capo_bedrock_agentcore_control.types.consent_portal_sources
    import capo_bedrock_agentcore_control.types.consent_portal_status
    import capo_bedrock_agentcore_control.types.portal_url_type


class ConsentPortalSummary(TypedDict, closed=True):
    sources: "capo_bedrock_agentcore_control.types.consent_portal_sources.ConsentPortalSources"
    """<p>The resources served by the consent portal.</p>"""
    consent_portal_arn: "capo_bedrock_agentcore_control.types.consent_portal_arn_type.ConsentPortalArnType"
    """<p>The Amazon Resource Name (ARN) of the consent portal.</p>"""
    consent_portal_id: "capo_bedrock_agentcore_control.types.consent_portal_id_type.ConsentPortalIdType"
    """<p>The unique identifier of the consent portal.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp for when the consent portal was created.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
    ]
    """<p>The description of the consent portal.</p>"""
    name: "capo_bedrock_agentcore_control.types.consent_portal_name_type.ConsentPortalNameType"
    """<p>The name of the consent portal.</p>"""
    portal_url: NotRequired[
        "capo_bedrock_agentcore_control.types.portal_url_type.PortalUrlType"
    ]
    """<p>The URL used to access the consent portal.</p>"""
    status: (
        "capo_bedrock_agentcore_control.types.consent_portal_status.ConsentPortalStatus"
    )
    """<p>The current status of the consent portal.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp for when the consent portal was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsentPortalSummary) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.consent_portal_sources

    out["sources"] = (
        capo_bedrock_agentcore_control.types.consent_portal_sources.serialize_json(
            value["sources"]
        )
    )
    out["consentPortalArn"] = value["consent_portal_arn"]
    out["consentPortalId"] = value["consent_portal_id"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    if "portal_url" in value:
        out["portalUrl"] = value["portal_url"]
    import capo_bedrock_agentcore_control.types.consent_portal_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.consent_portal_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConsentPortalSummary:
    out: ConsentPortalSummary = {}  # type: ignore[typeddict-item]
    if data.get("sources") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_sources

        out["sources"] = (
            capo_bedrock_agentcore_control.types.consent_portal_sources.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("ConsentPortalSummary.sources required")
    if data.get("consentPortalArn") is not None:
        out["consent_portal_arn"] = data["consentPortalArn"]
    else:
        raise DeserializationError("ConsentPortalSummary.consent_portal_arn required")
    if data.get("consentPortalId") is not None:
        out["consent_portal_id"] = data["consentPortalId"]
    else:
        raise DeserializationError("ConsentPortalSummary.consent_portal_id required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ConsentPortalSummary.created_at required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConsentPortalSummary.name required")
    if data.get("portalUrl") is not None:
        out["portal_url"] = data["portalUrl"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.consent_portal_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.consent_portal_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ConsentPortalSummary.status required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("ConsentPortalSummary.updated_at required")
    return out

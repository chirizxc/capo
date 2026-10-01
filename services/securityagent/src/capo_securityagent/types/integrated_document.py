"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedDocument``."""

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError


class IntegratedDocument(TypedDict, closed=True):
    integration_id: "str"
    """<p>The identifier of the integration that provides access to the document.</p>"""
    resource_id: "str"
    """<p>The provider-specific resource identifier for the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedDocument) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> IntegratedDocument:
    out: IntegratedDocument = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("IntegratedDocument.integration_id required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("IntegratedDocument.resource_id required")
    return out

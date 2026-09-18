"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGroupProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.group_identifier


class CreateGroupProfileInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the group profile is created.</p>"""
    group_identifier: NotRequired[
        "capo_datazone.types.group_identifier.GroupIdentifier"
    ]
    """<p>The identifier of the group for which the group profile is created.</p>"""
    role_principal_arn: NotRequired["str"]
    """<p>The ARN of the IAM role that will be associated with the group profile. This role defines the permissions that group members will assume when accessing Amazon DataZone resources.</p>"""
    client_token: NotRequired["str"]
    """<p> A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupProfileInput) -> dict:
    out: dict = {}
    if "group_identifier" in value:
        out["groupIdentifier"] = value["group_identifier"]
    if "role_principal_arn" in value:
        out["rolePrincipalArn"] = value["role_principal_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateGroupProfileInput:
    out: CreateGroupProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("groupIdentifier") is not None:
        out["group_identifier"] = data["groupIdentifier"]
    if data.get("rolePrincipalArn") is not None:
        out["role_principal_arn"] = data["rolePrincipalArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

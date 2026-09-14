"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.role_arn
    import capo_datazone.types.single_sign_on


class UpdateDomainInput(TypedDict, closed=True):
    identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon Web Services domain that is to be updated.</p>"""
    description: NotRequired["str"]
    """<p>The description to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    single_sign_on: NotRequired["capo_datazone.types.single_sign_on.SingleSignOn"]
    """<p>The single sign-on option to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    domain_execution_role: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The domain execution role to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    service_role: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The service role of the domain.</p>"""
    name: NotRequired["str"]
    """<p>The name to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "single_sign_on" in value:
        import capo_datazone.types.single_sign_on

        out["singleSignOn"] = capo_datazone.types.single_sign_on.serialize_json(
            value["single_sign_on"]
        )
    if "domain_execution_role" in value:
        out["domainExecutionRole"] = value["domain_execution_role"]
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateDomainInput:
    out: UpdateDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("singleSignOn") is not None:
        import capo_datazone.types.single_sign_on

        out["single_sign_on"] = capo_datazone.types.single_sign_on.deserialize_json(
            data["singleSignOn"]
        )
    if data.get("domainExecutionRole") is not None:
        out["domain_execution_role"] = data["domainExecutionRole"]
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out

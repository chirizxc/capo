"""Generated from Smithy shape ``com.amazonaws.workmail#OrganizationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.domain_name
    import capo_workmail.types.organization_id
    import capo_workmail.types.organization_name
    import capo_workmail.types.string


class OrganizationSummary(TypedDict, closed=True):
    organization_id: NotRequired["capo_workmail.types.organization_id.OrganizationId"]
    """<p>The identifier associated with the organization.</p>"""
    alias: NotRequired["capo_workmail.types.organization_name.OrganizationName"]
    """<p>The alias associated with the organization.</p>"""
    default_mail_domain: NotRequired["capo_workmail.types.domain_name.DomainName"]
    """<p>The default email domain associated with the organization.</p>"""
    error_message: NotRequired["capo_workmail.types.string.String"]
    """<p>The error message associated with the organization. It is only present if unexpected behavior has occurred with regards to the organization. It provides insight or solutions regarding unexpected behavior.</p>"""
    state: NotRequired["capo_workmail.types.string.String"]
    """<p>The state associated with the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationSummary) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "default_mail_domain" in value:
        out["DefaultMailDomain"] = value["default_mail_domain"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationSummary:
    out: OrganizationSummary = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    if data.get("DefaultMailDomain") is not None:
        out["default_mail_domain"] = data["DefaultMailDomain"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    return out

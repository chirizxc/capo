"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetQualificationsAssociationDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.partner_identifier


class GetQualificationsAssociationDetailsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog in which to look up the qualifications association. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQualificationsAssociationDetailsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQualificationsAssociationDetailsRequest:
    out: GetQualificationsAssociationDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "GetQualificationsAssociationDetailsRequest.catalog required"
        )
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "GetQualificationsAssociationDetailsRequest.identifier required"
        )
    return out

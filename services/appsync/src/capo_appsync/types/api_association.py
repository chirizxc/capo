"""Generated from Smithy shape ``com.amazonaws.appsync#ApiAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.association_status
    import capo_appsync.types.domain_name
    import capo_appsync.types.string


class ApiAssociation(TypedDict, closed=True):
    domain_name: NotRequired["capo_appsync.types.domain_name.DomainName"]
    """<p>The domain name.</p>"""
    api_id: NotRequired["capo_appsync.types.string.String"]
    """<p>The API ID.</p>"""
    association_status: NotRequired[
        "capo_appsync.types.association_status.AssociationStatus"
    ]
    """<p>Identifies the status of an association.</p> <ul> <li> <p> <b>PROCESSING</b>: The API association is being created. You cannot modify association requests during processing.</p> </li> <li> <p> <b>SUCCESS</b>: The API association was successful. You can modify associations after success.</p> </li> <li> <p> <b>FAILED</b>: The API association has failed. You can modify associations after failure.</p> </li> </ul>"""
    deployment_detail: NotRequired["capo_appsync.types.string.String"]
    """<p>Details about the last deployment status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiAssociation) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "api_id" in value:
        out["apiId"] = value["api_id"]
    if "association_status" in value:
        import capo_appsync.types.association_status

        out["associationStatus"] = capo_appsync.types.association_status.serialize_json(
            value["association_status"]
        )
    if "deployment_detail" in value:
        out["deploymentDetail"] = value["deployment_detail"]
    return out


def deserialize_json(data: dict) -> ApiAssociation:
    out: ApiAssociation = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("apiId") is not None:
        out["api_id"] = data["apiId"]
    if data.get("associationStatus") is not None:
        import capo_appsync.types.association_status

        out["association_status"] = (
            capo_appsync.types.association_status.deserialize_json(
                data["associationStatus"]
            )
        )
    if data.get("deploymentDetail") is not None:
        out["deployment_detail"] = data["deploymentDetail"]
    return out

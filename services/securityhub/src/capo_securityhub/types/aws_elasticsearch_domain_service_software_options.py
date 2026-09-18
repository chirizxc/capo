"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticsearchDomainServiceSoftwareOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsElasticsearchDomainServiceSoftwareOptions(TypedDict, closed=True):
    automated_update_date: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The epoch time when the deployment window closes for required updates. After this time, Amazon OpenSearch Service schedules the software upgrade automatically.</p>"""
    cancellable: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether a request to update the domain can be canceled.</p>"""
    current_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the service software that is currently installed on the domain.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A more detailed description of the service software status.</p>"""
    new_version: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The most recent version of the service software.</p>"""
    update_available: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether a service software update is available for the domain.</p>"""
    update_status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the service software update. Valid values are as follows:</p> <ul> <li> <p> <code>COMPLETED</code> </p> </li> <li> <p> <code>ELIGIBLE</code> </p> </li> <li> <p> <code>IN_PROGRESS</code> </p> </li> <li> <p> <code>NOT_ELIGIBLE</code> </p> </li> <li> <p> <code>PENDING_UPDATE</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticsearchDomainServiceSoftwareOptions) -> dict:
    out: dict = {}
    if "automated_update_date" in value:
        out["AutomatedUpdateDate"] = value["automated_update_date"]
    if "cancellable" in value:
        out["Cancellable"] = value["cancellable"]
    if "current_version" in value:
        out["CurrentVersion"] = value["current_version"]
    if "description" in value:
        out["Description"] = value["description"]
    if "new_version" in value:
        out["NewVersion"] = value["new_version"]
    if "update_available" in value:
        out["UpdateAvailable"] = value["update_available"]
    if "update_status" in value:
        out["UpdateStatus"] = value["update_status"]
    return out


def deserialize_json(data: dict) -> AwsElasticsearchDomainServiceSoftwareOptions:
    out: AwsElasticsearchDomainServiceSoftwareOptions = {}  # type: ignore[typeddict-item]
    if data.get("AutomatedUpdateDate") is not None:
        out["automated_update_date"] = data["AutomatedUpdateDate"]
    if data.get("Cancellable") is not None:
        out["cancellable"] = data["Cancellable"]
    if data.get("CurrentVersion") is not None:
        out["current_version"] = data["CurrentVersion"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("NewVersion") is not None:
        out["new_version"] = data["NewVersion"]
    if data.get("UpdateAvailable") is not None:
        out["update_available"] = data["UpdateAvailable"]
    if data.get("UpdateStatus") is not None:
        out["update_status"] = data["UpdateStatus"]
    return out

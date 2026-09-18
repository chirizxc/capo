"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadContact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.email
    import capo_partnercentral_selling.types.job_title
    import capo_partnercentral_selling.types.name
    import capo_partnercentral_selling.types.phone_number


class LeadContact(TypedDict, closed=True):
    business_title: "capo_partnercentral_selling.types.job_title.JobTitle"
    """<p>The lead contact's business title or job role associated with the engagement.</p>"""
    email: "capo_partnercentral_selling.types.email.Email"
    """<p>The lead contact's email address associated with the engagement.</p>"""
    first_name: "capo_partnercentral_selling.types.name.Name"
    """<p>The lead contact's first name associated with the engagement.</p>"""
    last_name: "capo_partnercentral_selling.types.name.Name"
    """<p>The lead contact's last name associated with the engagement.</p>"""
    phone: NotRequired["capo_partnercentral_selling.types.phone_number.PhoneNumber"]
    """<p>The lead contact's phone number associated with the engagement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadContact) -> dict:
    out: dict = {}
    out["BusinessTitle"] = value["business_title"]
    out["Email"] = value["email"]
    out["FirstName"] = value["first_name"]
    out["LastName"] = value["last_name"]
    if "phone" in value:
        out["Phone"] = value["phone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadContact:
    out: LeadContact = {}  # type: ignore[typeddict-item]
    if data.get("BusinessTitle") is not None:
        out["business_title"] = data["BusinessTitle"]
    else:
        raise DeserializationError("LeadContact.business_title required")
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("LeadContact.email required")
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    else:
        raise DeserializationError("LeadContact.first_name required")
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    else:
        raise DeserializationError("LeadContact.last_name required")
    if data.get("Phone") is not None:
        out["phone"] = data["Phone"]
    return out

"""Generated from Smithy shape ``com.amazonaws.account#AlternateContact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.alternate_contact_type
    import capo_account.types.email_address
    import capo_account.types.name
    import capo_account.types.phone_number
    import capo_account.types.title


class AlternateContact(TypedDict, closed=True):
    name: NotRequired["capo_account.types.name.Name"]
    """<p>The name associated with this alternate contact.</p>"""
    title: NotRequired["capo_account.types.title.Title"]
    """<p>The title associated with this alternate contact.</p>"""
    email_address: NotRequired["capo_account.types.email_address.EmailAddress"]
    """<p>The email address associated with this alternate contact.</p>"""
    phone_number: NotRequired["capo_account.types.phone_number.PhoneNumber"]
    """<p>The phone number associated with this alternate contact.</p>"""
    alternate_contact_type: NotRequired[
        "capo_account.types.alternate_contact_type.AlternateContactType"
    ]
    """<p>The type of alternate contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlternateContact) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "title" in value:
        out["Title"] = value["title"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "alternate_contact_type" in value:
        out["AlternateContactType"] = value["alternate_contact_type"]
    return out


def deserialize_json(data: dict) -> AlternateContact:
    out: AlternateContact = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("AlternateContactType") is not None:
        out["alternate_contact_type"] = data["AlternateContactType"]
    return out

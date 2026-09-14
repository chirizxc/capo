"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FieldSourceProfileIds``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_source_id_map
    import capo_customer_profiles.types.uuid


class FieldSourceProfileIds(TypedDict, closed=True):
    account_number: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the account number field to be merged. </p>"""
    additional_information: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the additional information field to be merged.</p>"""
    party_type: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the party type field to be merged.</p>"""
    business_name: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the business name field to be merged.</p>"""
    first_name: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the first name field to be merged.</p>"""
    middle_name: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the middle name field to be merged.</p>"""
    last_name: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the last name field to be merged.</p>"""
    birth_date: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the birthdate field to be merged.</p>"""
    gender: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the gender field to be merged.</p>"""
    phone_number: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the phone number field to be merged.</p>"""
    mobile_phone_number: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the mobile phone number field to be merged.</p>"""
    home_phone_number: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the home phone number field to be merged.</p>"""
    business_phone_number: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the business phone number field to be merged.</p>"""
    email_address: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the email address field to be merged.</p>"""
    personal_email_address: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the personal email address field to be merged.</p>"""
    business_email_address: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the party type field to be merged.</p>"""
    address: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the party type field to be merged.</p>"""
    shipping_address: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the shipping address field to be merged.</p>"""
    mailing_address: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the mailing address field to be merged.</p>"""
    billing_address: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the billing type field to be merged.</p>"""
    attributes: NotRequired[
        "capo_customer_profiles.types.attribute_source_id_map.AttributeSourceIdMap"
    ]
    """<p>A unique identifier for the attributes field to be merged.</p>"""
    profile_type: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the profile type field to be merged.</p>"""
    engagement_preferences: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>A unique identifier for the engagement preferences field to be merged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldSourceProfileIds) -> dict:
    out: dict = {}
    if "account_number" in value:
        out["AccountNumber"] = value["account_number"]
    if "additional_information" in value:
        out["AdditionalInformation"] = value["additional_information"]
    if "party_type" in value:
        out["PartyType"] = value["party_type"]
    if "business_name" in value:
        out["BusinessName"] = value["business_name"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "middle_name" in value:
        out["MiddleName"] = value["middle_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "birth_date" in value:
        out["BirthDate"] = value["birth_date"]
    if "gender" in value:
        out["Gender"] = value["gender"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "mobile_phone_number" in value:
        out["MobilePhoneNumber"] = value["mobile_phone_number"]
    if "home_phone_number" in value:
        out["HomePhoneNumber"] = value["home_phone_number"]
    if "business_phone_number" in value:
        out["BusinessPhoneNumber"] = value["business_phone_number"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "personal_email_address" in value:
        out["PersonalEmailAddress"] = value["personal_email_address"]
    if "business_email_address" in value:
        out["BusinessEmailAddress"] = value["business_email_address"]
    if "address" in value:
        out["Address"] = value["address"]
    if "shipping_address" in value:
        out["ShippingAddress"] = value["shipping_address"]
    if "mailing_address" in value:
        out["MailingAddress"] = value["mailing_address"]
    if "billing_address" in value:
        out["BillingAddress"] = value["billing_address"]
    if "attributes" in value:
        import capo_customer_profiles.types.attribute_source_id_map

        out["Attributes"] = (
            capo_customer_profiles.types.attribute_source_id_map.serialize_json(
                value["attributes"]
            )
        )
    if "profile_type" in value:
        out["ProfileType"] = value["profile_type"]
    if "engagement_preferences" in value:
        out["EngagementPreferences"] = value["engagement_preferences"]
    return out


def deserialize_json(data: dict) -> FieldSourceProfileIds:
    out: FieldSourceProfileIds = {}  # type: ignore[typeddict-item]
    if data.get("AccountNumber") is not None:
        out["account_number"] = data["AccountNumber"]
    if data.get("AdditionalInformation") is not None:
        out["additional_information"] = data["AdditionalInformation"]
    if data.get("PartyType") is not None:
        out["party_type"] = data["PartyType"]
    if data.get("BusinessName") is not None:
        out["business_name"] = data["BusinessName"]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("MiddleName") is not None:
        out["middle_name"] = data["MiddleName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("BirthDate") is not None:
        out["birth_date"] = data["BirthDate"]
    if data.get("Gender") is not None:
        out["gender"] = data["Gender"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("MobilePhoneNumber") is not None:
        out["mobile_phone_number"] = data["MobilePhoneNumber"]
    if data.get("HomePhoneNumber") is not None:
        out["home_phone_number"] = data["HomePhoneNumber"]
    if data.get("BusinessPhoneNumber") is not None:
        out["business_phone_number"] = data["BusinessPhoneNumber"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("PersonalEmailAddress") is not None:
        out["personal_email_address"] = data["PersonalEmailAddress"]
    if data.get("BusinessEmailAddress") is not None:
        out["business_email_address"] = data["BusinessEmailAddress"]
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    if data.get("ShippingAddress") is not None:
        out["shipping_address"] = data["ShippingAddress"]
    if data.get("MailingAddress") is not None:
        out["mailing_address"] = data["MailingAddress"]
    if data.get("BillingAddress") is not None:
        out["billing_address"] = data["BillingAddress"]
    if data.get("Attributes") is not None:
        import capo_customer_profiles.types.attribute_source_id_map

        out["attributes"] = (
            capo_customer_profiles.types.attribute_source_id_map.deserialize_json(
                data["Attributes"]
            )
        )
    if data.get("ProfileType") is not None:
        out["profile_type"] = data["ProfileType"]
    if data.get("EngagementPreferences") is not None:
        out["engagement_preferences"] = data["EngagementPreferences"]
    return out

"""Generated from Smithy shape ``com.amazonaws.pinpoint#NumberValidateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string


class NumberValidateResponse(TypedDict, closed=True):
    carrier: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The carrier or service provider that the phone number is currently registered with. In some countries and regions, this value may be the carrier or service provider that the phone number was originally registered with.</p>"""
    city: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the city where the phone number was originally registered.</p>"""
    cleansed_phone_number_e164: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The cleansed phone number, in E.164 format, for the location where the phone number was originally registered.</p>"""
    cleansed_phone_number_national: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The cleansed phone number, in the format for the location where the phone number was originally registered.</p>"""
    country: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the country or region where the phone number was originally registered.</p>"""
    country_code_iso2: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region where the phone number was originally registered.</p>"""
    country_code_numeric: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The numeric code for the country or region where the phone number was originally registered.</p>"""
    county: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the county where the phone number was originally registered.</p>"""
    original_country_code_iso2: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, that was sent in the request body.</p>"""
    original_phone_number: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The phone number that was sent in the request body.</p>"""
    phone_type: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The description of the phone type. Valid values are: MOBILE, LANDLINE, VOIP, INVALID, PREPAID, and OTHER.</p>"""
    phone_type_code: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The phone type, represented by an integer. Valid values are: 0 (mobile), 1 (landline), 2 (VoIP), 3 (invalid), 4 (other), and 5 (prepaid).</p>"""
    timezone: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The time zone for the location where the phone number was originally registered.</p>"""
    zip_code: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The postal or ZIP code for the location where the phone number was originally registered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberValidateResponse) -> dict:
    out: dict = {}
    if "carrier" in value:
        out["Carrier"] = value["carrier"]
    if "city" in value:
        out["City"] = value["city"]
    if "cleansed_phone_number_e164" in value:
        out["CleansedPhoneNumberE164"] = value["cleansed_phone_number_e164"]
    if "cleansed_phone_number_national" in value:
        out["CleansedPhoneNumberNational"] = value["cleansed_phone_number_national"]
    if "country" in value:
        out["Country"] = value["country"]
    if "country_code_iso2" in value:
        out["CountryCodeIso2"] = value["country_code_iso2"]
    if "country_code_numeric" in value:
        out["CountryCodeNumeric"] = value["country_code_numeric"]
    if "county" in value:
        out["County"] = value["county"]
    if "original_country_code_iso2" in value:
        out["OriginalCountryCodeIso2"] = value["original_country_code_iso2"]
    if "original_phone_number" in value:
        out["OriginalPhoneNumber"] = value["original_phone_number"]
    if "phone_type" in value:
        out["PhoneType"] = value["phone_type"]
    if "phone_type_code" in value:
        out["PhoneTypeCode"] = value["phone_type_code"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "zip_code" in value:
        out["ZipCode"] = value["zip_code"]
    return out


def deserialize_json(data: dict) -> NumberValidateResponse:
    out: NumberValidateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Carrier") is not None:
        out["carrier"] = data["Carrier"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("CleansedPhoneNumberE164") is not None:
        out["cleansed_phone_number_e164"] = data["CleansedPhoneNumberE164"]
    if data.get("CleansedPhoneNumberNational") is not None:
        out["cleansed_phone_number_national"] = data["CleansedPhoneNumberNational"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("CountryCodeIso2") is not None:
        out["country_code_iso2"] = data["CountryCodeIso2"]
    if data.get("CountryCodeNumeric") is not None:
        out["country_code_numeric"] = data["CountryCodeNumeric"]
    if data.get("County") is not None:
        out["county"] = data["County"]
    if data.get("OriginalCountryCodeIso2") is not None:
        out["original_country_code_iso2"] = data["OriginalCountryCodeIso2"]
    if data.get("OriginalPhoneNumber") is not None:
        out["original_phone_number"] = data["OriginalPhoneNumber"]
    if data.get("PhoneType") is not None:
        out["phone_type"] = data["PhoneType"]
    if data.get("PhoneTypeCode") is not None:
        out["phone_type_code"] = data["PhoneTypeCode"]
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    if data.get("ZipCode") is not None:
        out["zip_code"] = data["ZipCode"]
    return out

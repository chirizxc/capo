"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.string0_to255


class UpdateAddress(TypedDict, closed=True):
    address1: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The first line of a customer address.</p>"""
    address2: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The second line of a customer address.</p>"""
    address3: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The third line of a customer address.</p>"""
    address4: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The fourth line of a customer address.</p>"""
    city: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The city in which a customer lives.</p>"""
    county: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The county in which a customer lives.</p>"""
    state: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The state in which a customer lives.</p>"""
    province: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The province in which a customer lives.</p>"""
    country: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The country in which a customer lives.</p>"""
    postal_code: NotRequired["capo_customer_profiles.types.string0_to255.string0To255"]
    """<p>The postal code of a customer address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAddress) -> dict:
    out: dict = {}
    if "address1" in value:
        out["Address1"] = value["address1"]
    if "address2" in value:
        out["Address2"] = value["address2"]
    if "address3" in value:
        out["Address3"] = value["address3"]
    if "address4" in value:
        out["Address4"] = value["address4"]
    if "city" in value:
        out["City"] = value["city"]
    if "county" in value:
        out["County"] = value["county"]
    if "state" in value:
        out["State"] = value["state"]
    if "province" in value:
        out["Province"] = value["province"]
    if "country" in value:
        out["Country"] = value["country"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    return out


def deserialize_json(data: dict) -> UpdateAddress:
    out: UpdateAddress = {}  # type: ignore[typeddict-item]
    if data.get("Address1") is not None:
        out["address1"] = data["Address1"]
    if data.get("Address2") is not None:
        out["address2"] = data["Address2"]
    if data.get("Address3") is not None:
        out["address3"] = data["Address3"]
    if data.get("Address4") is not None:
        out["address4"] = data["Address4"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("County") is not None:
        out["county"] = data["County"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("Province") is not None:
        out["province"] = data["Province"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    return out
